from aiogram import filters, types, Router
from aiogram.utils.markdown import (
    hbold, hitalic, hpre, hunderline, hstrikethrough,
    hlink, hblockquote, hide_link
)
from keyboards.inline.yonalishKeyboard import yonalish
router = Router()

@router.message(filters.Command("start"))
async def command_start_handler(msg: types.Message):
    print(msg.from_user.id)
    await msg.answer(f"👋 {hbold('Assalomu alaykum', msg.from_user.first_name)}!\n\n🏫 Al Farg'oniy o'quv markazi botiga xush kelibsiz!")
    await msg.answer("Quyidagi bo'limlardan birini tanlang:", reply_markup=yonalish)
