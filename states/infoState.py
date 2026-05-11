from aiogram.filters.state import State, StatesGroup

class InfoState(StatesGroup):
    name = State()
    phone = State()
    course = State()

