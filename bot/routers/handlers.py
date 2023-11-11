import datetime
import re

from aiogram import F, Router, enums, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from django.utils.translation import gettext_lazy as _

from bot.filters.states import GetData
from bot.keyboards.keyboards import location_btn, menu_keyboard, plantes_btn
from users.models import User
from diagnosis.models import Diagnosis
from django.conf import settings
from aiogram.client.session.aiohttp import AiohttpSession
bot_session_ = AiohttpSession()


router_handler = Router()

# @router_handler.message(Command("start"))
@router_handler.message(F.text == "💊 Kasallikni tekshirish")
async def send_welcome(message: types.Message):
    await message.reply("O'simlikni tanlang", reply_markup=plantes_btn)


@router_handler.message(F.text == "🌾 Bug'doy")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply("Bug'doyzor manzilini yuboring", reply_markup=location_btn)
    await state.set_state(GetData.location)


@router_handler.message(GetData.location, F.location)
async def get_location(message: types.Message, state: FSMContext, user: User):
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
async def get_day(message: types.Message, state: FSMContext):
    await state.update_data(day=message.text)
    print(re.match("\b\d{1,2}/\d{1,2}/\d{4}\b", message.text))
    await message.answer("Bug'doyni hozirgi rasmini yuboring")
    await state.set_state(GetData.photo)




@router_handler.message(GetData.photo, F.text)
async def get_location(message: types.Message, state: FSMContext):
    await message.answer("Bug'doyni rasmini yuboring")
    await state.set_state(GetData.photo)
    
# @router_handler.message(GetData.photo, F.photo)
@router_handler.message( F.photo)
async def get_location(message: types.Message, state: FSMContext, user: User):
    
    bot_ = Bot(settings.BOT_TOKEN, parse_mode="HTML", session=bot_session_)

    file_id = message.photo[-1].file_id
    
    # Download the photo
    photo_path = await bot_.get_file(file_id)
    photo = await bot_.download_file(photo_path.file_path)
    
    # Save the photo locally
    local_path = f'media/diagnosis/{file_id}.jpg'  # Change the directory and file name as needed
    with open(local_path, 'wb') as photo_file:
        photo_file.write(photo.read())
    await bot_session_.close()
    
    diagnosis = Diagnosis()
    # diagnosis.user = user
    diagnosis.image = f'diagnosis/{file_id}.jpg'
    diagnosis.name = "Bug'doy"
    diagnosis.description = "Bug'doy"
    diagnosis.predict_disease()
    await diagnosis.asave()
    
    await message.answer("Saqlandi", reply_markup=menu_keyboard)
    # await state.finish()
    
    
