from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💊 Kasallikni tekshirish"), KeyboardButton(text="Maslahat olish")],
        [KeyboardButton(text="📞 Aloqa")],
    ],
    resize_keyboard=True,
)


plantes_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌾 Bug'doy"),
        ],
            [
            KeyboardButton(text="🌿 Kakain")
            ],
            [
            KeyboardButton(text="🌳 Geroyin")
        ]
    ],
    resize_keyboard=True,
)


location_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True),
        ]
    ],
    resize_keyboard=True,
)
