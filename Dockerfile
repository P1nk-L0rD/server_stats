# Используем официальный Python образ версии 3.10
FROM python:3.10-slim

RUN apt-get update && apt-get upgrade -y

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Команда для запуска uvicorn
CMD ["uvicorn", "main.api:app", "--host", "0.0.0.0", "--port", "8110"]
