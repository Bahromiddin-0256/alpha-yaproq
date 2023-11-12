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

bot_session_ = AiohttpSession()

router_handler = Router()


# @router_handler.message(Command("start"))
@router_handler.message(F.text == "💊 Kasallikni tekshirish")
async def send_welcome(message: types.Message):
    await message.reply("O'simlikni tanlang", reply_markup=plantes_btn)


@router_handler.message(F.text == "🌾 Bug'doy")
async def send_welcome(message: types.Message, state: GetData):
    await message.reply("Bug'doyzor manzilini yuboring", reply_markup=location_btn)
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
    await message.reply(f"Bug'doyzor manzili: {longitude}, {latitude}")

    await message.answer("Bug'doy qachon ekilganligini kiriting (25/11/2023)", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(GetData.day)


@router_handler.message(GetData.day, F.text)
async def get_day(message: types.Message, state: GetData):
    await state.update_data(day=message.text)
    print(re.match("\b\d{1,2}/\d{1,2}/\d{4}\b", message.text))
    await message.answer("Bug'doyni hozirgi rasmini yuboring")
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
    # diagnosis.user = user
    diagnosis.image = f"diagnosis/{file_id}.jpg"
    diagnosis.name = "Bug'doy"
    diagnosis.description = "Bug'doy"
    # diagnosis.predict_disease()
    await diagnosis.asave()
    ds_lev = await DiseaseLevel.objects.filter(level=diagnosis.result).afirst()
    if ds_lev:
        await message.answer(
            f"{ds_lev.level} - {ds_lev.description} \n Losing Percentage: {ds_lev.percent}% \n\n"
            f"How to treat {ds_lev.treatment if ds_lev.treatment else ''}",
            reply_markup=menu_keyboard,
        )

    else:
        await message.answer(f"Kasallik topilmadi holat - {diagnosis.result}", reply_markup=menu_keyboard)
    await state.clear()


@router_handler.message(F.text == "🌡 Havo harorati va namlik")
async def air_humidity(message: types.Message, state: WeatherData):
    txt = "Yaqindagi Havo harorati va namlikni bilish uchun joriy locatsiyangizni yuboring"
    await message.reply(txt, reply_markup=location_btn)
    await state.set_state(WeatherData.location)


@router_handler.message(F.location, WeatherData.location)
async def get_location(message: types.Message, state: WeatherData, user: User):
    longitude = message.location.longitude
    latitude = message.location.latitude
    weather = WEATHER_CLIENT.get_forecast(longitude, latitude)

    name = weather["city"]["name"]

    # txt = f"{name}\n"
    txt = "Yaqin 5 kundagi kutilayotgan ob-havo namliklari:\n\n"
    for hour_ in range(0, len(weather["list"]), 8):
        hour = weather["list"][hour_]
        if hour["main"]["humidity"] >= 30:
            txt += f"🕔 {hour['dt_txt'].split(' ')[0]} da \n   ☁️  namlik: {hour['main']['humidity']} \n    temp: {hour['main']['temp']}\n"
    warning = "Siz ushbu vaqtlarda 90% va undan ortiq namlikda hosilingizga e'tiborliroq bo'lishingizni so'rayman!"
    await message.answer(txt)
    await message.answer(warning, reply_markup=menu_keyboard)

    await state.clear()


@router_handler.message(GetData.photo, F.text)
async def get_location(message: types.Message, state: GetData):
    await message.answer("Bug'doyni rasmini yuboring")
    await state.set_state(GetData.photo)
