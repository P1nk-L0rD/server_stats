# Используем официальный Python образ версии 3.10
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости (например, requirements.txt) в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Команда для запуска uvicorn
CMD ["uvicorn", "main.api:app", "--host", "0.0.0.0", "--port", "8110"]
