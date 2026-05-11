from aiogram import types, Router
from keyboards.inline.yonalishKeyboard import yonalish
router = Router()

@router.message()
async def echo_handler(msg: types.Message):
    await msg.answer(f"Bizda {msg.text} buyrug'i yo'q 😁\nIltimos biz taklif qilgan bo'limlardan tanlang! 👇")
    await msg.answer("Quyidagi bo'limlardan birini tanlang:", reply_markup=yonalish)
