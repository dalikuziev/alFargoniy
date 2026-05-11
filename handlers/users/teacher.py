from aiogram import types, Router, F
from aiogram.utils.markdown import hbold
router = Router()

@router.callback_query(F.data == "teacher")
async def callback_handler(call: types.CallbackQuery):
    teachers = f"👨‍🏫 {hbold("Bizning malakali ustozlar jamoasi:")}\n\n"
    teachers += f"{hbold("Diyorbek")} - Dasturlash backend\n"
    teachers += f"{hbold("Samandar")} - Dasturlash frontend\n"
    teachers += f"{hbold("Muhammadqodir")} - Kompyuter savodxonligi\n"
    teachers += f"{hbold("Opa")} - Ingliz tili va Karea tili\n"
    await call.message.edit_text(teachers)

