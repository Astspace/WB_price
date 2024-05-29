from aiogram import Bot, Dispatcher
import asyncio
from tg.handlers import router
from database.models_db import async_main

bot = Bot(token='7437243653:AAFc0jBzBTA0V8_cl3OZ1T1OoGdCiQQqDW4')
dp = Dispatcher()

async def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")