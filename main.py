import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from data.config import TOKEN
from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.info import router as info_router
from handlers.users.teacher import router as teacher_router
from handlers.users.echo import router as echo_router
dp = Dispatcher()

async def main():
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(info_router)
    dp.include_router(teacher_router)
    dp.include_router(echo_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())
