from aiogram import types
from keyboards import menu_keyboard, plantes_btn, location_btn
from config import ADMIN, dp
# import fsmcontext
from aiogram.dispatcher import FSMContext
import datetime

# Start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum. Men sizga o'simliklarni kasalliklarini aniqlashga, ularni davolashga va kelajakda kelishi mumkin bo'lgan kasalliklarni oldini olishga yordam beraman.", reply_markup=menu_keyboard)
    
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Bot orqali siz o'simliklarni kasalliklarini aniqlashga, ularni davolashga va kelajakda kelishi mumkin bo'lgan kasalliklarni oldini olishga yordam beraman.", reply_markup=menu_keyboard)
    
@dp.message_handler(text='💊 Kasallikni tekshirish')
async def send_welcome(message: types.Message):
    await message.reply("O'simlikni tanlang", reply_markup=plantes_btn)
    
@dp.message_handler(text='🌾 Bug\'doy', state=None)
async def send_welcome(message: types.Message, state=FSMContext):
    await message.reply("Bug'doyzor manzilini yuboring", reply_markup=location_btn)
    await state.set_state("location")
    
# @dp.message_handler(state="location", content_types=types.ContentTypes.LOCATION)
# async def send_welcome(message: types.Message, state=FSMContext):
#     longitude = message.location.longitude
#     latitude = message.location.latitude
#     date_time = datetime.datetime.now()
    
#     await message.reply(f"Bug'doyzor manzili: {longitude}, {latitude}\nSana va vaqt: {date_time}")
#     await state.update_data(longitude=longitude, latitude=latitude, date_time=date_time)
    
    # await message.reply("Bug'doyzor manzili qabul qilindi", reply_markup=menu_keyboard)
    # await state.reset_state()
    