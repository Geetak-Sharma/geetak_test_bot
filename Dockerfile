FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install aiogram

CMD ["python", "bot.py"]
