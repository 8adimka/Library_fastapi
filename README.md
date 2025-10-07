# FastAPI Library - Библиотечный REST API

REST API для управления библиотекой и заметками, реализованное на FastAPI с PostgreSQL.

## 🚀 Быстрый старт

### Запуск через Docker Compose (рекомендуется)

```bash
# Клонируйте репозиторий
git clone https://github.com/8adimka/Library_fastapi
cd Library_fastapi

# Запустите проект
docker-compose up --build -d

# API будет доступен на http://localhost:8000
# Документация Swagger: http://localhost:8000/docs
```

### Ручной запуск

```bash
# Установите зависимости
poetry install

# Запустите миграции
alembic upgrade head

# Запустите сервер
poetry run uvicorn app.main:app --reload
```

## 📚 API Документация

### 🔹 API Заметок (Notes)

#### Создание заметки

```bash
curl -X POST http://localhost:8000/notes/ \
  -H "Content-Type: application/json" \
  -d '{"note": "Моя первая заметка", "description": "Описание заметки"}'
```

**Ответ:** `{"id": 1}`

#### Получение всех заметок

```bash
curl -X GET http://localhost:8000/notes/ | cat
```

**Ответ:** `[{"id": 1, "note": "Моя первая заметка", "description": "Описание заметки"}]`

#### Получение конкретной заметки

```bash
curl -X GET http://localhost:8000/notes/1/ | cat
```

**Ответ:** `{"id": 1, "note": "Моя первая заметка", "description": "Описание заметки"}`

#### Обновление заметки

```bash
curl -X PUT http://localhost:8000/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"note": "Обновленная заметка", "description": "Новое описание"}'
```

#### Удаление заметки

```bash
curl -X DELETE http://localhost:8000/notes/1/
```

### 🔹 API Библиотеки

#### Авторы

```bash
# Создание автора
curl -X POST http://localhost:8000/api/library/authors/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Лев Толстой"}'

# Получение всех авторов
curl -X GET http://localhost:8000/api/library/authors/ | cat

# Получение автора по ID
curl -X GET http://localhost:8000/api/library/authors/1/ | cat
```

#### Залы

```bash
# Создание зала
curl -X POST http://localhost:8000/api/library/halls/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Основной зал"}'

# Получение всех залов
curl -X GET http://localhost:8000/api/library/halls/ | cat
```

#### Книги

```bash
# Создание книги
curl -X POST http://localhost:8000/api/library/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Война и мир", "hall_id": 1, "author_ids": [1]}'

# Получение всех книг
curl -X GET http://localhost:8000/api/library/books/ | cat

# Получение книги по ID
curl -X GET http://localhost:8000/api/library/books/1/ | cat
```

#### Читатели

```bash
# Создание читателя
curl -X POST http://localhost:8000/api/library/readers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Иван Иванов"}'

# Получение всех читателей
curl -X GET http://localhost:8000/api/library/readers/ | cat
```

#### Выдача и возврат книг

```bash
# Выдача книги читателю
curl -X POST "http://localhost:8000/api/library/borrow/?reader_id=1&book_id=1"

# Возврат книги
curl -X POST "http://localhost:8000/api/library/return/?reader_id=1&book_id=1"
```

## 🛠 Утилиты

### Обработка логов

```bash
# Создайте тестовый лог-файл
echo "asfga asdabasdjabsf _ _ _ has3l asd has3l" > test_log.txt

# Подсчет уникальных кодов
python scripts/parse_logs.py test_log.txt

# Сортировка по количеству вхождений
python scripts/parse_logs.py test_log.txt --sort
```

**Вывод:**

```
has3l : 2
asfga : 1
```

### Нагрузочное тестирование

```bash
# Тестирование API заметок
python scripts/testNotesREST.py \
  --url http://localhost:8000 \
  --ops 100 \
  --add_ratio 0.7 \
  --workers 5
```

## 🧪 Тестирование

```bash
# Запуск всех тестов
poetry run pytest

# Запуск конкретных тестов
poetry run pytest tests/test_notes_api.py
poetry run pytest tests/test_library_api.py
poetry run pytest tests/test_logs_parser.py
```

## 📊 Проверка работоспособности

### Быстрая проверка всех функций

```bash
# Проверка API
curl -X GET http://localhost:8000/ | cat

# Проверка документации
curl -X GET http://localhost:8000/docs | head -20

# Создание тестовых данных
curl -X POST http://localhost:8000/notes/ \
  -H "Content-Type: application/json" \
  -d '{"note": "Тестовая заметка", "description": "Проверка работы API"}' | cat

# Проверка сохранения данных
curl -X GET http://localhost:8000/notes/ | cat
```

## 🗄 База данных

### Миграции

```bash
# Создание новой миграции
alembic revision --autogenerate -m "описание изменений"

# Применение миграций
alembic upgrade head

# Откат миграции
alembic downgrade -1
```

### Постоянное хранение

- Данные сохраняются в PostgreSQL через Docker volume `pgdata`
- После перезапуска контейнеров данные сохраняются
- Для разработки используется SQLite

## 🔧 Технические детали

### Стек технологий

- **Backend**: FastAPI, Python 3.11
- **База данных**: PostgreSQL (production), SQLite (тесты)
- **ORM**: SQLAlchemy
- **Миграции**: Alembic
- **Контейнеризация**: Docker, Docker Compose
- **Тестирование**: Pytest

### Особенности реализации

- Полная валидация данных через Pydantic
- Обработка ошибок с корректными HTTP статусами
- Пагинация для списков
- Многопоточное нагрузочное тестирование
- Автоматическая документация OpenAPI

## 📁 Структура проекта

```
library-fastapi/
├── app/
│   ├── api/routers/          # Роутеры API
│   ├── models.py             # Модели SQLAlchemy
│   ├── schemas.py            # Схемы Pydantic
│   ├── crud.py               # CRUD операции
│   └── main.py               # Точка входа
├── scripts/
│   ├── parse_logs.py         # Обработка логов
│   └── testNotesREST.py      # Нагрузочное тестирование
├── tests/                    # Тесты
├── alembic/                  # Миграции базы данных
└── docker-compose.yml        # Docker конфигурация
```

## 📞 Контакты

- Автор: Medintsev Vadim (github.com/8adimka)
- Проект: FastAPI Library API
