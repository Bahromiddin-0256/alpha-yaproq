import datetime

from aiogram import F, Router, enums, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from django.utils.translation import gettext_lazy as _

from bot.filters.states import GetData
from bot.keyboards.keyboards import location_btn, menu_keyboard, plantes_btn
from users.models import User

router_handler = Router()


# @router_handler.message(Command("start"))
@router_handler.message(F.text == "💊 Kasallikni tekshirish")
async def send_welcome(message: types.Message):
    await message.reply("O'simlikni tanlang", reply_markup=plantes_btn)


@router_handler.message(F.text == "🌾 Bug'doy")
async def send_welcome(message: types.Message, state=FSMContext):
    await message.reply("Bug'doyzor manzilini yuboring", reply_markup=location_btn)
    await state.set_state(GetData.location)


@router_handler.message(GetData.location, F.location)
async def get_location(message: types.Message, state=FSMContext):
    longitude = message.location.longitude
    latitude = message.location.latitude

    await state.update_data(
        lon=longitude,
        lat=latitude,
    )
    await message.reply(f"Bug'doyzor manzili: {longitude}, {latitude}")

    await message.answer("Bug'doy qachon ekilganligini kiriting (25/11/2023)", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(GetData.day)


@router_handler.message(GetData.day, F.text)
async def get_day(message: types.Message, state=FSMContext):
    await state.update_data(day=message.text)
    await message.answer("Bug'doyni hozirgi rasmini yuboring")
    await state.set_state(GetData.photo)


@router_handler.message(GetData.photo, F.photo)
async def get_location(message: types.Message, state=FSMContext):
    photo = message.photo
    print(photo)


@router_handler.message(GetData.photo, F.text)
async def get_location(message: types.Message, state=FSMContext):
    await message.answer("Bug'doyni rasmini yuboring")
    await state.set_state(GetData.photo)
