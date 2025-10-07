# 📚 Документация API - FastAPI Library

Полная документация по всем эндпоинтам REST API для управления библиотекой и заметками.

## 🔑 Базовый URL

```
http://localhost:8000
```

## 📝 API Заметок (Notes)

### Создание заметки

- **Метод**: `POST /notes/`
- **Статус**: 201 Created
- **Описание**: Создает новую заметку

**Тело запроса:**

```json
{
  "note": "Текст заметки (до 120 символов)",
  "description": "Описание заметки (до 1024 символов, опционально)"
}
```

**Пример:**

```bash
curl -X POST http://localhost:8000/notes/ \
  -H "Content-Type: application/json" \
  -d '{"note": "Купить молоко", "description": "Не забыть купить молоко в магазине"}'
```

**Ответ:**

```json
{"id": 1}
```

### Получение всех заметок

- **Метод**: `GET /notes/`
- **Статус**: 200 OK
- **Описание**: Возвращает список всех заметок

**Пример:**

```bash
curl -X GET http://localhost:8000/notes/ | cat
```

**Ответ:**

```json
[
  {
    "id": 1,
    "note": "Купить молоко",
    "description": "Не забыть купить молоко в магазине"
  }
]
```

### Получение конкретной заметки

- **Метод**: `GET /notes/{note_id}/`
- **Статус**: 200 OK или 404 Not Found
- **Описание**: Возвращает информацию о конкретной заметке

**Пример:**

```bash
curl -X GET http://localhost:8000/notes/1/ | cat
```

**Ответ:**

```json
{
  "id": 1,
  "note": "Купить молоко",
  "description": "Не забыть купить молоко в магазине"
}
```

### Обновление заметки

- **Метод**: `PUT /notes/{note_id}/`
- **Статус**: 200 OK или 404 Not Found
- **Описание**: Обновляет существующую заметку

**Тело запроса:**

```json
{
  "note": "Обновленный текст заметки",
  "description": "Обновленное описание"
}
```

**Пример:**

```bash
curl -X PUT http://localhost:8000/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"note": "Купить молоко и хлеб", "description": "Добавить хлеб в список покупок"}'
```

### Удаление заметки

- **Метод**: `DELETE /notes/{note_id}/`
- **Статус**: 200 OK или 404 Not Found
- **Описание**: Удаляет заметку по ID

**Пример:**

```bash
curl -X DELETE http://localhost:8000/notes/1/
```

## 📚 API Библиотеки

### Авторы

#### Создание автора

- **Метод**: `POST /api/library/authors/`
- **Статус**: 201 Created

**Тело запроса:**

```json
{
  "name": "Имя автора"
}
```

**Пример:**

```bash
curl -X POST http://localhost:8000/api/library/authors/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Александр Пушкин"}'
```

#### Получение всех авторов

- **Метод**: `GET /api/library/authors/`
- **Параметры**: `limit`, `offset` (пагинация)

**Пример:**

```bash
curl -X GET "http://localhost:8000/api/library/authors/?limit=10&offset=0" | cat
```

#### Получение автора по ID

- **Метод**: `GET /api/library/authors/{author_id}/`

**Пример:**

```bash
curl -X GET http://localhost:8000/api/library/authors/1/ | cat
```

### Залы

#### Создание зала

- **Метод**: `POST /api/library/halls/`

**Тело запроса:**

```json
{
  "name": "Название зала"
}
```

**Пример:**

```bash
curl -X POST http://localhost:8000/api/library/halls/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Читальный зал"}'
```

#### Получение всех залов

- **Метод**: `GET /api/library/halls/`

### Книги

#### Создание книги

- **Метод**: `POST /api/library/books/`
- **Статус**: 201 Created

**Тело запроса:**

```json
{
  "title": "Название книги",
  "hall_id": 1,
  "author_ids": [1, 2]
}
```

**Пример:**

```bash
curl -X POST http://localhost:8000/api/library/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Евгений Онегин", "hall_id": 1, "author_ids": [1]}'
```

#### Получение всех книг

- **Метод**: `GET /api/library/books/`
- **Параметры**: `limit`, `offset` (пагинация)

#### Получение книги по ID

- **Метод**: `GET /api/library/books/{book_id}/`

### Читатели

#### Создание читателя

- **Метод**: `POST /api/library/readers/`

**Тело запроса:**

```json
{
  "name": "Имя читателя"
}
```

**Пример:**

```bash
curl -X POST http://localhost:8000/api/library/readers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Петр Сидоров"}'
```

### Выдача и возврат книг

#### Выдача книги

- **Метод**: `POST /api/library/borrow/`
- **Параметры**: `reader_id`, `book_id`

**Пример:**

```bash
curl -X POST "http://localhost:8000/api/library/borrow/?reader_id=1&book_id=1"
```

**Ответ:**

```json
{
  "id": 1,
  "reader_id": 1,
  "book_id": 1,
  "borrowed_at": "2024-01-01T12:00:00",
  "returned_at": null
}
```

#### Возврат книги

- **Метод**: `POST /api/library/return/`
- **Параметры**: `reader_id`, `book_id`

**Пример:**

```bash
curl -X POST "http://localhost:8000/api/library/return/?reader_id=1&book_id=1"
```

## 🛠 Утилиты

### Обработка логов

**Скрипт**: `scripts/parse_logs.py`

**Использование:**

```bash
# Базовый подсчет
python scripts/parse_logs.py logfile.txt

# Сортировка по количеству вхождений
python scripts/parse_logs.py logfile.txt --sort
```

**Формат кода ошибки**: любые 5 буквенных или численных символов, отделенные пробелами

**Пример входного файла:**

```
asfga asdabasdjabsf _ _ _ has3l asd has3l
```

**Вывод:**

```
has3l : 2
asfga : 1
```

### Нагрузочное тестирование

**Скрипт**: `scripts/testNotesREST.py`

**Параметры:**

- `--url`: URL API сервера
- `--ops`: Общее количество операций
- `--add_ratio`: Отношение добавлений к удалениям (0.0-1.0)
- `--workers`: Количество рабочих потоков

**Пример:**

```bash
python scripts/testNotesREST.py \
  --url http://localhost:8000 \
  --ops 1000 \
  --add_ratio 0.7 \
  --workers 10
```

## ⚠️ Коды ошибок

### Общие ошибки

- `200 OK` - Успешное выполнение
- `201 Created` - Успешное создание
- `400 Bad Request` - Неверные параметры запроса
- `404 Not Found` - Ресурс не найден
- `500 Internal Server Error` - Внутренняя ошибка сервера

### Специфичные ошибки библиотеки

- `400 Book is already borrowed` - Книга уже выдана
- `400 Active borrowing not found` - Активная выдача не найдена

## 🔍 Примеры использования

### Полный рабочий цикл заметок

```bash
# 1. Создание заметки
curl -X POST http://localhost:8000/notes/ \
  -H "Content-Type: application/json" \
  -d '{"note": "Изучить FastAPI", "description": "Изучить документацию FastAPI"}'

# 2. Получение всех заметок
curl -X GET http://localhost:8000/notes/ | cat

# 3. Обновление заметки
curl -X PUT http://localhost:8000/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"note": "Изучить FastAPI и SQLAlchemy", "description": "Расширить знания"}'

# 4. Удаление заметки
curl -X DELETE http://localhost:8000/notes/1/
```

### Полный рабочий цикл библиотеки

```bash
# 1. Создание автора
curl -X POST http://localhost:8000/api/library/authors/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Михаил Булгаков"}'

# 2. Создание зала
curl -X POST http://localhost:8000/api/library/halls/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Художественная литература"}'

# 3. Создание книги
curl -X POST http://localhost:8000/api/library/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Мастер и Маргарита", "hall_id": 1, "author_ids": [1]}'

# 4. Создание читателя
curl -X POST http://localhost:8000/api/library/readers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Анна Петрова"}'

# 5. Выдача книги
curl -X POST "http://localhost:8000/api/library/borrow/?reader_id=1&book_id=1"

# 6. Возврат книги
curl -X POST "http://localhost:8000/api/library/return/?reader_id=1&book_id=1"
```

## 📊 Мониторинг

### Проверка здоровья API

```bash
curl -X GET http://localhost:8000/ | cat
```

### Документация Swagger

```
http://localhost:8000/docs
```

### Схема OpenAPI

```
http://localhost:8000/openapi.json
```

---

**📞 Для дополнительной информации обратитесь к README.md или исходному коду проекта.**
