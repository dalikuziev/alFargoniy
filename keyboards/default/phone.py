from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="contact", request_contact=True),
        ]
    ]
)
