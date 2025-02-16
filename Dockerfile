FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir aiogram fastapi uvicorn

# Run the bot
CMD ["python", "bot.py"]

