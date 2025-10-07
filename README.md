# FastAPI Library

- fastapi-library/
- ├─ .env
- ├─ docker-compose.yml
- ├─ Dockerfile
- ├─ pyproject.toml
- ├─ README.md
- ├─ app/
- │  ├─ __init__.py
- │  ├─ main.py
- │  ├─ core.py
- │  ├─ db.py
- │  ├─ models.py
- │  ├─ schemas.py
- │  ├─ crud.py
- │  ├─ api/
- │  │  ├─ __init__.py
- │  │  ├─ deps.py
- │  │  ├─ routers/
- │  │  │  ├─ __init__.py
- │  │  │  ├─ library.py
- │  │  │  └─ notes.py
- │  └─ utils/
- │     └─ logs_parser.py
- ├─ scripts/
- │  ├─ parse_logs.py
- │  └─ testNotesREST.py

Запуск (требуется Docker и docker-compose):

1. Скопируйте `.env` (пример в проекте) и при необходимости измените значения.
2. Построить и запустить контейнеры:

```bash
docker-compose up --build
````

3. API будет доступен на `http://localhost:8000`

   - Документация OpenAPI: `http://localhost:8000/docs`

Скрипты:

- `scripts/parse_logs.py` — подсчёт 5-символьных кодов в логе.
- `scripts/testNotesREST.py` — нагрузочное тестирование `notes` API.

Примечание: данные хранятся в PostgreSQL volume `pgdata` и сохраняются между перезапусками.

- После первого запуска контейнера (docker-compose up --build) база создастся автоматически благодаря `Base.metadata.create_all`.
- Данные будут сохраняться в Docker volume `pgdata`.
- Для production лучше заменить автоматическое `create_all` на Alembic миграции, но пока и так сойдёт.

## Быстрый старт

1. Клонируйте репозиторий и установите зависимости:
   ```bash
   git clone <repo_url>
   cd library-fastapi
   poetry install
   ```

2. Запустите проект через Docker Compose:
   ```bash
   docker-compose up -d
   ```
   API будет доступен на `http://localhost:8000`

3. Запуск FastAPI вручную (без Docker):
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

4. Миграции Alembic:
   ```bash
   alembic upgrade head
   ```

5. Тестирование:
   ```bash
   poetry run pytest
   ```

6. Парсинг логов:
   ```bash
   python scripts/parse_logs.py test_log.txt --sort
   ```

7. Нагрузочное тестирование:
   ```bash
   python scripts/testNotesREST.py
   ```

## Восстановление данных
- Все данные хранятся в базе Postgres (docker-compose) или SQLite (тесты).
- После перезапуска контейнеров данные сохраняются.

## Миграции Alembic
- Для создания/обновления схемы используйте команды Alembic:
   ```bash
   alembic revision --autogenerate -m "init"
   alembic upgrade head
   ```

## Пагинация
- Для списков (книги, авторы, заметки) поддерживается пагинация через параметры `limit` и `offset`.

## Логирование и обработка ошибок
- Все ошибки возвращаются с корректными статус-кодами и сообщениями.
- Важные действия логируются.

## Контакты
- Автор: 8adimka
