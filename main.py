# Завдання 1
#==============================================================================================
# Є словник з логінами(ключ) та паролями(значення) користувачів.
# Реалізуйте програму яка дозволяє:
# завантажити дані з файлу
# зберегти дані у файл
# додати нового користувача
# видалити користувача
# зміна паролю
# вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.
import json
#
# users_data = {
#     "12345": "12345",
#     "login1": "admin123",
#     "login2": "user123",
# }
#
# def save_data(logins, filename="logins.json"):
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(logins, file, indent=4)
#
#
# def load_data(filename="logins.json"):
#     with open(filename, "r", encoding="utf-8") as file:
#         logins = json.load(file)
#
#     return logins
#
#
# def add_new_user():
#     user_login = input("Enter login to add: ")
#     user_password = input("Enter password to add: ")
#
#     if user_login not in users_data:
#         users_data[user_login] = user_password
#     else:
#         print("This login is already exist")
#
#
# def delete_user():
#     user_login = input("Enter user login: ")
#
#     if user_login in users_data:
#         users_data.pop(user_login)
#     else:
#         print("User login not found")
#
#
# def change_password():
#     user_login = input("Enter user login: ")
#
#     if user_login in users_data:
#         new_password = input("Enter new password: ")
#         users_data[user_login] = new_password
#         print("Password has changed")
#
#     else:
#         print("User login no found")
#
#
# def enter_to_system():
#     user_login = input("Enter login: ")
#     user_password = input("Enter password: ")
#
#     if user_login not in users_data:
#         print("Wrong login")
#         return
#
#     if users_data[user_login] != user_password:
#         print("Wrong password")
#         return
#
#     print("You entered to the system!")
#
#
# add_new_user()
# delete_user()
# change_password()
# enter_to_system()
# save_data(users_data)
# print(load_data())

# Завдання 2
#==============================================================================================
# Створіть клас Cart
# Атрибути:
# user – ім’я користувача
# items – список товарів
# total – загальна ціна
# Методи:
# add(item, price) – добавити товар у кошик
# delete(item, price) – видалити товар з кошика
# info() – вивести інформацію про кошик
# save(fiename) – зберегти дані у файл(за
# замовчуванням cart.json)
# load(fiename) – завантажити дані з файла(за
# замовчуванням cart.json)

# class Cart:
#     def __init__(self, user, items):
#         self.user = user
#         self.items = items
#         self.total = 0
#
#     def add(self, item, price):
#         self.items[item] = price
#         print("Product has been added")
#
#     def delete(self, item):
#         if item in self.items:
#             self.items.pop(item)
#             print("Product is removed from your cart")
#
#         else:
#             print("Product is not in your cart")
#
#     def info(self):
#         print("Your cart")
#         self.total = 0
#
#         for item, price in self.items.items():
#             print(f"Product: {item}. Price: {price}")
#             self.total += price
#
#         print(f"Total price: {self.total}")
#
#     def save_cart_data(self):
#         with open("cart.json", "r", encoding="utf-8") as file:
#             users_carts = json.load(file)
#
#         cart_data = {
#             "items": self.items,
#             "total": self.total
#         }
#
#         users_carts[self.user] = cart_data
#
#         with open("cart.json", "w", encoding="utf-8") as file:
#             json.dump(users_carts, file, indent=4)
#
#     def load_cart_data(self):
#         with open("cart.json", "r", encoding="utf-8") as file:
#             cart_data = json.load(file)
#
#         user_data = cart_data[self.user]
#         self.items = user_data["items"]
#         self.total = user_data["total"]
#
#         return user_data
#
#
# cart1 = Cart("John", {"apple": 20, "banana": 15})
# cart1.add("mango", 25)
# cart1.delete("apple")
# cart1.info()
# cart1.save_cart_data()
# print(cart1.load_cart_data())

# Завдання 3
#==============================================================================================
# Створіть файл settings.json з базовими налаштуваннями програми, наприклад графічного інтерфейсу:
# розмір зображення – 500х600
# колір фону – сірий
# колір кнопок – світлосірий
# розміщення кнопок – [100, 50]
# інструкція користувачу
# Напишіть код, де завантажується налаштування і створюються відповідні змінні
# import time
#
# settings = {
#     "background_color": "gray",
#     "image_size": 200,
#     "buttons_color": "red",
#     "buttons_location": [100, 50],
#     "instruction": "Some text for user",
# }
#
# def save_data():
#         with open("settings.json", "w", encoding="utf-8") as file:
#             json.dump(settings, file, indent=4)
#
# def load_data():
#         with open("settings.json", "r", encoding="utf-8") as file:
#             settings_data = json.load(file)
#
#         return settings_data
#
#
# save_data()
# print("Import your settings...")
# time.sleep(3)
# print("Your settings have been setup")
#
# settings_data = load_data()
#
# for item, value in settings_data.items():
#     print(f"Name: {item}. Value: {value}")
