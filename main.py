# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

# class Cart:
#     def __init__(self, client, items):
#         self.client = client
#         self.items = items
#
#     def add_product(self):
#         product_name = input("Enter product name to add: ")
#         self.items.append(product_name)
#         print("Product has been added to the cart")
#
#     def delete_product(self):
#         product_name = input("Enter product name to delete: ")
#
#         if product_name in self.items:
#             self.items.remove(product_name)
#             print("Product has been deleted from the cart")
#         else:
#             print("Product not found")
#
#     def show_info(self):
#         if len(self.items):
#             print("Product name")
#             for product in self.items:
#                 print(product)
#         else:
#             print("Cart is empty")
#
#
# products = []
# cart1 = Cart("John", products)
#
# while True:
#     try:
#         user_choice = int(input("Choose service - add product(1), delete product(2), show cart info(3), exit(4): "))
#
#         if 5 > user_choice > 0:
#             if user_choice == 1:
#                 cart1.add_product()
#
#             elif user_choice == 2:
#                 cart1.delete_product()
#
#             elif user_choice == 3:
#                 cart1.show_info()
#
#             else:
#                 print("Exit from program")
#                 break
#
#     except ValueError:
#         print("Enter valid number")
#
# =============================================================================================
# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки зменшити відсотків передається як параметр),
# якщо він опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.

# class Phone:
#     def __init__(self, number, battery_level):
#         self.number = number
#         self.battery_level = battery_level
#
#     def decrease_battery_level(self, procent):
#         if procent <= self.battery_level:
#             self.battery_level -= procent
#
#             print("Battery level has been decreased")
#             print(f"Battery level is {self.battery_level}%")
#
#             if self.battery_level < 20:
#                 print("Warning: battery level is lower than 20%")
#
#         else:
#             print("Procent couldn't be bigger than current battery level")
#
#     def show_phone_info(self):
#         print(f"Number: {self.number}. Battery level: {self.battery_level}%")
#
#
# phone1 = Phone(12345, 80)
# while True:
#     try:
#         user_choice = int(input("Choose service - decrease battery level(1), show phone info(2), exit(3): "))
#
#         if 4 > user_choice > 0:
#             if user_choice == 1:
#                 try:
#                     procent = int(input("Enter procent to decrease: "))
#                     if procent > 0:
#                         phone1.decrease_battery_level(procent)
#
#                     else:
#                         print("Enter valid number")
#
#                 except ValueError:
#                     print("Enter valid value")
#
#             elif user_choice == 2:
#                 phone1.show_phone_info()
#
#             else:
#                 print("Exit from program")
#                 break
#
#     except ValueError:
#         print("Enter valid value")
