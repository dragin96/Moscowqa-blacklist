# Используем официальный образ Python в качестве базового
FROM python:3.8-slim

# Установим переменную окружения для не использования буфера при выводе
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл Pipfile и Pipfile.lock в контейнер
COPY Pipfile Pipfile.lock /app/

# Устанавливаем pipenv и зависимости
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

# Копируем все остальные файлы в контейнер
COPY . /app/

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Запуск приложения через pipenv с использованием uvicorn из виртуального окружения
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
