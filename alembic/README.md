# Alembic миграции

## Быстрый старт

1. Инициализация alembic (если не выполнено):
   ```bash
   alembic init alembic
   ```
2. Создание ревизии:
   ```bash
   alembic revision --autogenerate -m "init"
   ```
3. Применение миграций:
   ```bash
   alembic upgrade head
   ```

## Конфигурация
- Файл alembic/env.py уже настроен для работы с моделями из app.db
- DATABASE_URL берётся из переменных окружения
