# Завдання 1
#===================================================================================================
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач.
# Реалізуйте функціонал:
# додати новий товар
# вивести список товарів
# зберегти дані через json
# зберегти дані через pickle
# завантажити дані через json
# завантажити дані через pickle
import json
import pickle
import os


class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.items = []

    def add_item(self):
        item_name = input("Enter product name: ")
        item_price = float(input("Enter product price: "))
        item_brand = input("Enter product brand: ")

        item_data = {
            "name": item_name,
            "price": item_price,
            "brand": item_brand,
        }

        self.items.append(item_data)

    def show_cart(self):
        print(f"{self.user_name}'s products")

        for item in self.items:
            print(f"\tProduct data")
            print(f"\t Name: {item["name"]}")
            print(f"\t Price: {item["price"]}")
            print(f"\t Brand: {item["brand"]}")

    def save_data_json(self):
        # read exist data
        if os.path.exists("products.json"):
            with open("products.json", "r", encoding="utf-8") as file:
                users_data = json.load(file)

        # File products.json doesn't exist (first saving)
        else:
            users_data = {}

        users_data[self.user_name] = self.items

        with open("products.json", "w", encoding="utf-8") as file:
            json.dump(users_data, file, indent=4)

    def save_data_pickle(self):
        # read exist data
        if os.path.exists("products.pkl"):
            with open("products.pkl", "rb") as file:
                users_data = pickle.load(file)

        # File products.json doesn't exist (first saving)
        else:
            users_data = {}

        users_data[self.user_name] = self.items

        with open("products.pkl", "wb") as file:
            pickle.dump(users_data, file)

    def load_data_json(self):
        with open("products.json", "r", encoding="utf-8") as file:
            users_data = json.load(file)

            if self.user_name in users_data:
                self.items = users_data[self.user_name]

            else:
                self.items = []

    def load_data_pickle(self):
        with open("products.pkl", "rb") as file:
            users_data = pickle.load(file)
            self.items = users_data[self.user_name]


# Tests
cart1 = Cart("John")
cart1.add_item()
cart1.add_item()

cart1.show_cart()

cart1.save_data_json()
cart1.save_data_pickle()

cart1.load_data_json()
cart1.load_data_pickle()

cart1.show_cart()

cart2 = Cart("Maria")
cart2.add_item()
cart2.add_item()

cart2.show_cart()

cart2.save_data_json()
cart2.save_data_pickle()

cart2.load_data_json()
cart2.load_data_pickle()

cart2.show_cart()

# Завдання 2
#===================================================================================================
# Напишіть клас Student
# Атрибути:
# name – ім’я
# specialization – спеціалізація
# grades – список оцінок
# Методи:
# add_grade(grade) – додати нову оцінку
# show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Практичне завдання
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.