import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from fastapi import FastAPI, Request
import uvicorn

# Set Bot Token & Webhook URL
TOKEN = "7709450866:AAHymCobKs5PuN01OPB4bWMVVKTSBXW6Pl8"
WEBHOOK_URL = "https://renewed-kingfisher-dealshub-1d13ebf7.koyeb.app/webhook"

bot = Bot(token=TOKEN)
dp = Dispatcher()
app = FastAPI()

# ✅ Corrected Health Check Endpoint
@app.get("/health")
async def health():
    return {"status": "ok"}

# ✅ Telegram Webhook Endpoint
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    await dp.process_update(update)

# ✅ Bot Message Handler
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"You said: {message.text}")

# ✅ Setup Webhook Before Running the App
async def main():
    await bot.set_webhook(WEBHOOK_URL)
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())
