from aiogram import filters, types, Router
router = Router()

@router.message(filters.Command("help"))
async def command_help_handler(msg: types.Message):
    await msg.answer(f"Tinchlikmi {msg.from_user.first_name.title()}!")
    await msg.answer("Mening o'zimga yozing barcha savollaringizga javob olasiz\n"
                     "telegram: @dalikuziev\n"
                     "phone: +998992166020")
