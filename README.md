# Finance App

Desktop-приложение для учёта личных финансов.

## Возможности

- Добавление расходов
- Хранение данных в SQLite
- Аналитика расходов
- Графики по месяцам
- Просмотр последних операций
- GUI на Tkinter

---

## Технологии

- Python
- Tkinter
- SQLite
- Pandas
- Matplotlib

---

## Структура проекта

```text
finance-project/
│
├── data/               # Excel и база данных
├── ui/                 # Интерфейс
│
├── analysis.py         # Аналитика
├── database.py         # Работа с SQLite
├── repository.py       # SQL-запросы
├── services.py         # Бизнес-логика
├── main.py             # Точка входа