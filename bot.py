import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from fastapi import FastAPI
import uvicorn

TOKEN = os.getenv("TELEGRAM_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Set this to your Koyeb app URL

bot = Bot(token=TOKEN)
dp = Dispatcher()

app = FastAPI()

# Health check endpoint
@app.get("/")
async def health():
    return {"status": "ok"}

@app.post("/webhook")
async def telegram_webhook(update: dict):
    telegram_update = Update(**update)
    await dp.process_update(telegram_update)

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"You said: {message.text}")

async def main():
    await bot.set_webhook(WEBHOOK_URL + "/webhook")
    dp.run_app(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
