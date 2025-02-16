import os
import asyncio
import uvicorn
from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI
import threading

TOKEN = os.getenv("TELEGRAM_API_KEY")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# FastAPI app for health checks
app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "OK"}

async def start_bot():
    await dp.start_polling(bot)

def run_health_check():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Start FastAPI server in a separate thread
    health_thread = threading.Thread(target=run_health_check, daemon=True)
    health_thread.start()

    # Run the bot
    asyncio.run(start_bot())
