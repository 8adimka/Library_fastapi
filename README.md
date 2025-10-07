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

---
