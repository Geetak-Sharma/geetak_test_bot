import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("TELEGRAM_API_KEY")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"You said: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
