FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install aiogram fastapi uvicorn

CMD ["python", "bot.py"]
