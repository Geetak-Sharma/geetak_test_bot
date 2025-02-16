import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from fastapi import FastAPI, Request
import asyncio
import os

# Load your bot token here
BOT_TOKEN = "7709450866:AAHymCobKs5PuN01OPB4bWMVVKTSBXW6Pl8"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Initialize FastAPI
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        update = Update(**await request.json())
        await dp._process_update(update)  # Correcting method name for aiogram v3
    except Exception as e:
        logger.error(f"Error processing update: {e}")
    return {"status": "ok"}

@dp.message()
async def handle_message(message: types.Message):
    try:
        await message.answer("Hello! I'm your bot.")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
