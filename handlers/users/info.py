from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold
from states.infoState import InfoState
from keyboards.default.phone import phone
from data.config import ADMINS
router = Router()

@router.callback_query(F.data == "info")
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Barcha ma'lumotlaringizni to'liq kiriting!", cache_time=60)
    await call.message.answer("Ism va familiyangizni kiriting:")
    await call.message.delete()
    await state.set_state(InfoState.name)

@router.message(InfoState.name)
async def name_handler(msg: types.Message, state: FSMContext):
    global first_name
    first_name = msg.text.split()[0].title()
    await state.update_data(name=msg.text)
    await msg.answer(f"{first_name} telefon raqamingizni yuboring:", reply_markup=phone)
    await state.set_state(InfoState.phone)

@router.message(InfoState.phone)
async def phone_handler(msg: types.Message, state: FSMContext):
    if msg.contact is None:
        await msg.answer(f"{first_name} telefon nomeringiz to'g'ri yuborilmadi!")
        await state.set_state(InfoState.phone)
    elif msg.from_user.id == msg.contact.user_id:
        await state.update_data(phone=msg.contact.phone_number)
        await msg.answer(f"{first_name}!\n\n📚Qaysi yo'nalishga qiziqasiz?", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(InfoState.course)
    else:
        await msg.answer(f"{first_name} telefon nomeringiz most kelmadi!")
        await state.set_state(InfoState.phone)

@router.message(InfoState.course)
async def course_handler(msg: types.Message, state: FSMContext):
    await state.update_data(course=msg.text)
    await msg.answer(f"✅ {hbold("Arizangiz qabul qilindi!")}\n\nTez orada aloqaga chiqamiz.")
    data = await state.get_data()
    info = f"O'quvchi: {data["name"]}\n"
    info += f"Telefon nomer: {data["phone"]}\n"
    info += f"Course: {data["course"]}\n"
    for admin in ADMINS:
        await msg.bot.send_message(admin, info)
    await state.clear()

