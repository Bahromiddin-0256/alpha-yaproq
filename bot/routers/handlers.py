import re

from aiogram import Bot, F, Router, types
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.context import FSMContext
from django.conf import settings

from bot.filters.states import GetData, WeatherData
from bot.keyboards.keyboards import location_btn, menu_keyboard, plantes_btn
from common.weather import WEATHER_CLIENT
from diagnosis.models import Diagnosis, DiseaseLevel
from users.models import User
from diagnosis.processing import process_result
bot_session_ = AiohttpSession()

router_handler = Router()


# @router_handler.message(Command("start"))
@router_handler.message(F.text == "💊 Check the disease")
async def send_welcome(message: types.Message):
    await message.reply("Choose a plant", reply_markup=plantes_btn)


@router_handler.message(F.text == "🌾 Wheat")
async def send_welcome(message: types.Message, state: GetData):
    await message.reply("Submit the wheat field address", reply_markup=location_btn)
    await state.set_state(GetData.location)


@router_handler.message(GetData.location, F.location)
async def get_location(message: types.Message, state: GetData, user: User):
    longitude = message.location.longitude
    latitude = message.location.latitude

    await state.update_data(
        lon=longitude,
        lat=latitude,
    )
    user.latitude = latitude
    user.longitude = longitude
    await user.asave()
    # await message.reply(f"Wheat field address: {longitude}, {latitude}")

    # await message.answer("Enter when wheat is planted (25/11/2023)", reply_markup=types.ReplyKeyboardRemove())
#     await state.set_state(GetData.day)


# @router_handler.message(GetData.day, F.text)
# async def get_day(message: types.Message, state: GetData):
#     await state.update_data(day=message.text)
#     print(re.match("\b\d{1,2}/\d{1,2}/\d{4}\b", message.text))
    await message.answer("Submit a current photo of Wheat", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(GetData.photo)



@router_handler.message(GetData.photo, F.photo)
async def get_diagnosis(message: types.Message, state: GetData, user: User):
    bot_ = Bot(settings.BOT_TOKEN, parse_mode="HTML", session=bot_session_)

    file_id = message.photo[-1].file_id

    # Download the photo
    photo_path = await bot_.get_file(file_id)
    photo = await bot_.download_file(photo_path.file_path)

    # Save the photo locally
    local_path = f"media/diagnosis/{file_id}.jpg"  # Change the directory and file name as needed
    with open(local_path, "wb") as photo_file:
        photo_file.write(photo.read())
    await bot_session_.close()

    diagnosis = Diagnosis()
    diagnosis.user = user
    diagnosis.image = f"diagnosis/{file_id}.jpg"
    diagnosis.name = "Bug'doy"
    diagnosis.description = "Bug'doy"
    diagnosis.predict_disease()
    await diagnosis.asave()
    ds_lev = await DiseaseLevel.objects.filter(level=diagnosis.result).afirst()
    if ds_lev:
        await message.answer(
            f"{ds_lev.level} - {ds_lev.description} \n Losing Percentage: {ds_lev.percent}% \n\n"
            f"How to treat {ds_lev.treatment if ds_lev.treatment else ''}",
            reply_markup=menu_keyboard,
        )
       
        ## get user location
        longitude = user.longitude
        latitude = user.latitude
        
        weather = WEATHER_CLIENT.get_forecast(longitude, latitude)
        
        txt = "Expected humidity for the next 5 days:\n\n"
        i = 0
        weather_list = []
        humidity_list = []
        for hour_ in range(0, len(weather['list']), 8):
            i += 1
            hour = weather['list'][hour_]
            humidity = hour['main']['humidity']
            weather = 2 if hour['weather']['main'] == "Clear" else 1 if hour['weather']['main'] == "Rain" else 0
            weather_list.append(weather)
            humidity_list.append(humidity)
            if i == 2:
                break
            
        severity = ds_lev.percent
            
        res = process_result(weather_list, humidity_list, severity)
        for i in res:
            if i == "High":
                new_ = "Status:  🔴 "
            elif i == "Moderate":
                new_ = "Status:  🟡 "
            else:
                new_ = "Status: 🟢 "
            await message.answer(new_)
        
            # if hour['main']['humidity'] >= 0: ###  
            #     txt += f"🕔 {hour['dt_txt'].split(' ')[0]} da \n   ☁️  humidity: {hour['main']['humidity']} \n    🌡 temp: {hour['main']['temp']}\n"
        # warning = "I ask you to pay more attention to your harvest during these times with humidity of 80% and more!"

    else:
        await message.answer(f"Disease not found status - {diagnosis.result}", reply_markup=menu_keyboard)
    await state.clear()
    
   
    
    
    
    


@router_handler.message(F.text == "🌡 Air temperature and humidity")
async def air_humidity(message: types.Message, state: WeatherData):
    txt = "Submit your current location to find out the nearby Air temperature and humidity"
    await message.reply(txt, reply_markup=location_btn)
    await state.set_state(WeatherData.location)


@router_handler.message(F.location, WeatherData.location)
async def get_location(message: types.Message, state: WeatherData, user: User):
    longitude = message.location.longitude
    latitude = message.location.latitude
    weather = WEATHER_CLIENT.get_forecast(longitude, latitude)
    
    # name = weather['city']['name']
    
    # txt = f"{name}\n"
    txt = "Expected humidity for the next 5 days:\n\n"
    for hour_ in range(0, len(weather['list']), 8):
        hour = weather['list'][hour_]
        if hour['main']['humidity'] >= 50: #comment
            txt += f"🕔 {hour['dt_txt'].split(' ')[0]} da \n   ☁️  humidity: {hour['main']['humidity']} \n    🌡 temp: {hour['main']['temp']}\n"
    warning = "I ask you to pay more attention to your harvest during these times with humidity of 80% and more!"
    await message.answer(txt)
    await message.answer(warning, reply_markup=menu_keyboard)
    
    await state.clear()
    

@router_handler.message(F.text == "Get advice")
async def get_location(message: types.Message):

    kasallik1 = "I advise you to take precautionary measures to prevent this disease. \n\n"

    s = """
    We recommend following organic control methods in the early stages of a disease or when the crop is close to
    harvesting. In more advanced stages of a disease, please follow chemical control measures. Mixing or applying
    different products at the same time is not recommended.

``` Organic Control ```

Many biofungicides are available in the market. Products based on Bacillus pumilus applied at 7 to 14 days intervals
are effective against the fungus and are marketed by major actors of the industry.

``` Chemical Control ```

Always consider an integrated approach with preventive measures together with biological treatments if available.
 Foliar sprays of fungicides belonging to the strobilurin class provide effective protection against the disease when
 the application is done preventively. In already infected fields, use products belonging to the triazole family or
 mixes of both products."""
    await message.answer(kasallik1)
    await message.answer(s, reply_markup=menu_keyboard)
    
    
    
@router_handler.message(F.text == "📞 Contact")
async def get_location(message: types.Message):
    txt = "How can I contact the ALPHA team?\n\n"
    txt += "ALPHA team:\n\n"
    txt += "👨‍💻Sindarov Jo'rabek\n📞 Phone: +998 90 067 04 16\nTelegram: @sindarov_004\n\n"
    txt += "👨‍💻Mamatmusayev Jaloliddin\n📞 Phone: +998 93 297 74 19\nTelegram: @Jaloliddin_Mamatmusayev\n\n"
    txt += "👨‍💻Muhammadaliyev Nodirjon\n📞 Phone: +998 99 493 41 82\nTelegram: @Nodirjon2505\n\n"
    txt += "👨‍💻Ibragimov Bahromiddin\n📞 Phone: +998 94 561 19 14\nTelegram: @bahromiddin\n\n"
    txt += "👨‍💻Hasanov Diyorbek\n📞 Phone: +998 94 324 40 90\nTelegram: @khdiyorbek\n\n"
    
    await message.answer(txt, reply_markup=menu_keyboard)