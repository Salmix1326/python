# Модуль 14. Мережеве програмування
# Тема: Мережеве програмування. Частина 2
#===============================================================
# Завдання 1
# Напишіть сервер:
# ● шлях – /hello
# ● метод – POST
# Функція має повертати JSON об’єкт {"message": "Привіт з сервера!"}
# Запустіть сервер:
# ● host – localhost
# ● port – 8000
# uvicorn main:app --port 8000 –host localhost --reload
# Напишіть клієнта який робить запит на сервер
# from fastapi import FastAPI
#
#
# app = FastAPI()

# @app.post("/hello")
# def welcome():
#     return {"message": "Привіт з сервера!"}


# Завдання 2
#===================================================
# Напишіть сервер1:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8000
# Напишіть сервер2:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера2"}
# ● порт – 8001
# Запустіть обида сервери на localhost
# Напишіть клієнта який робить запита на обидва сервери
# from fastapi import FastAPI
#
#
# app = FastAPI()
#
# @app.get("/greeting")
# def hi():
#     return {"respond": "Привіт з сервера1"}


# Завдання 3
#===========================================================================
# Напишіть сервер з такими функціями
# ● hello
# ○ шлях – /hello/{name}
# ○ метод – POST
# ○ повертає {"message": "Привіт, {ім'я}!"}
# ● hello_json
# ○ шлях – /hello_json
# ○ метод – POST
# ○ повертає {"message": "Привіт, {ім'я}!"}
# Для hello_json напишіть модель за допомогою pydantic
# Запустіть сервер
# Напишіть клієнта який робить запити на сервер
# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# app = FastAPI()
#
# class NameModel(BaseModel):
#     name: str
#
# @app.post("/hello/{name}")
# def hello(name: str):
#     return {"message": f"Привіт, {name}!"}
#
#
# @app.post("/hello_json")
# def hello_json(data: NameModel):
#     return {"message": f"Привіт, {data.name}!"}


# Завдання 4
# Напишіть сервер для симуляції роботи бібліотеки.
# Дані про книги знаходяться у файлі books.json
# Напишіть модель на pydentic для книги з такими
# даними:
# ● id
# ● title
# ● author
# ● year
# ● pages
# Функціонал:
# 1. Отримання всіх книг
# ○ шлях – books
# ○ метод – GET
# 2. Отримання даних за ID книги
# ○ шлях – books/{book_id}
# ○ метод – GET
# 3. Додавання нової книги
# ○ шлях – books
# ○ метод – POST
# 4. Видалення книги за ID
# ○ шлях – books/{book_id}
# ○ метод – DELETE
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int

app = FastAPI()


@app.get("/books")
def get_all_books(filename: str = 'books.json'):
    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    return data


@app.post("/books")
def add_new(book_json: Book, filename: str = 'books.json'):
    if not os.path.exists(filename):
        data = {}
    else:
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    data[str(book_json.id)] = book_json.dict()

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return {"message": f"Книга '{book_json.title}' додана!"}
