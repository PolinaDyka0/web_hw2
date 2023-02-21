# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10


# Встановимо робочу директорію усередині контейнера
WORKDIR .

# Скопіюємо інші файли до робочої директорії контейнера
COPY . .

# Встановимо залежності усередині контейнера
RUN pip install -r requirements.txt

# Запустимо нашу програму всередині контейнера
CMD echo 'This is console bot'

ENTRYPOINT ["python", "menu.py"]

VOLUME ./data:/data
