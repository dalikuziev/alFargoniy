from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

yonalish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Kursga yozilish", callback_data="info"),
            InlineKeyboardButton(text="👨‍🏫 Ustozlar", callback_data="teacher"),
        ]
    ]
)
a = 1
