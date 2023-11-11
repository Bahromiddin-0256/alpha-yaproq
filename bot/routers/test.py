from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from django.utils.translation import gettext_lazy as _

from bot.filters.states import Registration, GetDisease
from bot.keyboards.keyboards import menu_keyboard, location_btn
from users.models import User

router = Router()


@router.message(Command("start"))
async def on_start(message: types.Message, user: User):
    await message.answer(
        "Assalomu alaykum. Men sizga o'simliklarni kasalliklarini aniqlashga, ularni davolashga va kelajakda kelishi mumkin bo'lgan kasalliklarni oldini olishga yordam beraman.",
        reply_markup=menu_keyboard,
    )


@router.message(Command("help"))
async def on_start(message: types.Message, user: User):
    await message.reply(
        "Bot orqali siz o'simliklarni kasalliklarini aniqlashga, ularni davolashga va kelajakda kelishi mumkin bo'lgan kasalliklarni oldini olishga yordam beraman.",
        reply_markup=menu_keyboard,
    )


@router.message(F.text == "Yaqin atrofdagi fermalarda nima gap?")
async def send_welcome(message: types.Message, state: FSMContext):
    txt = "Sizni fermangizga yaqinida qanday kasalliklar borligini bilish uchun joylashuvni yuboring"
    await message.reply(txt, reply_markup=location_btn)
    await state.set_state(GetDisease.location)
    
    
@router.message(F.location, GetDisease.location)
async def get_location(message: types.Message, state: FSMContext, user: User):
    longitude = message.location.longitude
    latitude = message.location.latitude

    await message.reply(f"Joylashuv: {longitude}, {latitude}")

    txt = "Sizga yaqin atrofdagi fermalarda quyidagi kasalliklar topilgan:"
    
    kasallik1 = "Sizdan shimoliy-sharq tomonida 2 km masofada bulgan fermalarda <b>Yellow rust</b> kasalligi topilgan. Kasallikning darajasi 30%. \n"
    kasallik1 += "Bu kasallikni oldini olish bo'yicha ehtiyotkorlik chorasi ko'rishni maslahat beraman. \n\n"
    
    
    s = """
    We recommend following organic control methods in the early stages of a disease or when the crop is close to harvesting. In more advanced stages of a disease, please follow chemical control measures. Mixing or applying different products at the same time is not recommended.

``` Organic Control ```

Many biofungicides are available in the market. Products based on Bacillus pumilus applied at 7 to 14 days intervals are effective against the fungus and are marketed by major actors of the industry.

``` Chemical Control ```

Always consider an integrated approach with preventive measures together with biological treatments if available. Foliar sprays of fungicides belonging to the strobilurin class provide effective protection against the disease when the application is done preventively. In already infected fields, use products belonging to the triazole family or mixes of both products."""
    await message.answer(txt)
    await message.answer(kasallik1)
    await message.answer(s, reply_markup=menu_keyboard)
    await state.clear()
    
    
    

@router.message(Command("help"))
async def start_register_user(message: types.Message, state: FSMContext):
    await message.reply(str(_("Ismingizni kiriting:")))
    await state.set_state(Registration.first_name)


@router.message(Registration.first_name)
async def registration_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.reply(str(_("Familiyangizni kiriting:")))
    await state.set_state(Registration.last_name)


@router.message(Registration.last_name)
async def registration_finish(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(str(_("Ro'yhatga olish yakunlandi.")))
    await message.answer(
        _("Ism: {first_name}\n").format(first_name=data.get("first_name"))
        + _("Familiya: {last_name}\n").format(last_name=message.text),
    )
    await state.clear()
