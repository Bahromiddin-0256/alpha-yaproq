from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💊 Check the disease"), KeyboardButton(text="Get advice")],
        [KeyboardButton(text="What's up with the nearby farms?")],
        [KeyboardButton(text="🌡 Air temperature and humidity")],
        [KeyboardButton(text="📞 Contact")],
    ],
    resize_keyboard=True,
)


plantes_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌾 Wheat"),
        ],
    ],
    resize_keyboard=True,
)


location_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Send location", request_location=True),
        ]
    ],
    resize_keyboard=True,
)
