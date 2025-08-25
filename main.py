# Завдання 2
# Створіть клас Телефон з атрибутами:
# максимальний обсяг пам’яті
# зайнята пам’ять
# чи включений(за замовчуванням False)
# встановлені додатки у вигляді словника, де ключ – назва додатку, значення – обсяг пам’яті
# Додайте методи:
# вивести інформацію про використання пам’яті
# видалити додаток
# встановити новий додаток, якщо пам’яті достатньо
# оновити додаток(нова версія може займати іншу кількість пам’яті)
# запустити додаток, якщо він є і якщо телефон вкючений
# включити телефон
# виключити телефон

# class Phone:
#     def __init__(self, max_memory_level, used_memory, apps: dict ):
#         self.max_memory_level = max_memory_level
#         self.apps = apps
#         self.used_memory = used_memory
#         self.is_active = False
#         for key, value in self.apps.items():
#             self.used_memory += value
#
#     def show_memory_info(self):
#         print(f"Max memory usage: {self.max_memory_level}")
#         print(f"Current memory usage: {self.used_memory}")
#
#     def delete_app(self, app_name):
#         if app_name in self.apps:
#             self.apps.pop(app_name)
#             print("App is deleted")
#             for key, value in self.apps.items():
#                 self.used_memory = 0
#                 self.used_memory += value
#         else:
#             print("App not found")
#
#     def install_app(self, new_app_name, new_app_memory):
#         current_memory_usage = sum(self.apps.values())
#
#         if (self.max_memory_level - current_memory_usage) >= new_app_memory:
#             self.apps[new_app_name] = new_app_memory
#             print(self.apps)
#             self.used_memory = 0
#             for key, value in self.apps.items():
#                 self.used_memory += value
#
#             print("App is installed")
#
#         else:
#             print("Not enough memory in phone")
#
#     def update_app(self, app_name):
#         if (self.max_memory_level - self.used_memory) > 10:
#             if app_name in self.apps:
#                 self.apps[app_name] += 10
#                 self.used_memory = 0
#                 for key, value in self.apps.items():
#                     self.used_memory += value
#                 print(f"{app_name} is updated")
#             else:
#                 print("App is not found")
#
#         else:
#             print("Not enough memory for update")
#
#     def play_app(self, app_name):
#         if app_name in self.apps and self.is_active:
#             print(f"{app_name} is playing")
#
#         else:
#             print("App not found or phone is not active")
#
#     def start_phone(self):
#         self.is_active = True
#         print("Phone is started")
#
#     def power_off_phone(self):
#         self.is_active = False
#         print("Phone is off")
#
# phone1 = Phone(250, 0, {"youtube": 20, "instagram":50})
# phone1.install_app("game",100)
# phone1.show_memory_info()
# phone1.start_phone()
# phone1.play_app("game")
# phone1.update_app("game")
# phone1.show_memory_info()

#=======================================================================================
# Завдання 3
# Створіть клас Автомобіль з атрибутами:
# марка
# пробіг
# рівень пального
# витрата пального(л/км)
# чи є справним(за замовчуванням True)
# Реалізуйте методи:
# проїхати певну відстань, має змінитись пробіг та рівень пального, якщо автомобіль справний та достатньо пального
# З ймовірністю 40% автомобіль може зламатись ремонт
# поповнення пального
# import random
#
#
# class Car:
#     def __init__(self, brand, mileage, fuel_level, fuel_consumption):
#         self.brand = brand
#         self.mileage = mileage
#         self.fuel_level = fuel_level
#         self.fuel_consumption = fuel_consumption
#         self.is_working_properly = True
#
#     def go_distance(self, kilometers):
#         if self.fuel_level > (self.fuel_consumption * (kilometers/100)):
#             self.mileage += kilometers
#             self.fuel_level -= (self.fuel_consumption * (kilometers/100))
#             print(f"You have driven {kilometers} kilometers")
#         else:
#             print(f"Not enough fuel for {kilometers} km")
#
#         random_value = random.randint(1, 100)
#
#         if random_value < 40:
#             print("The car broke down")
#             self.is_working_properly = False
#
#     def refuel_car(self, fuel_to_add):
#         self.fuel_level += fuel_to_add
#         print("Сar has been refueled")
#
#     def car_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Mileage: {self.mileage}")
#         print(f"Fuel Level: {self.fuel_level}")
#         print(f"Fuel Consumption l/km: {self.fuel_consumption}")
#
# car1 = Car("Mercedes",0,100,5)
# car1.go_distance(50)
# car1.car_info()
# car1.refuel_car(50)
# car1.car_info()
import random
from itertools import product


#========================================================================================
# Завдання 4
# Створіть клас Студент з атрибутами:
# ім’я
# словник з предметами, де ключ – назва предмету, значення – список оцінок
# Додайте методи:
# додати новий предмет
# видалити предмет
# вчити предмет(якщо отримана оцінка, то додати про це інформацію)
# отримати середню оцінку за конкретним предметом
# вивести загальну інформацію: ім’я та список предметів з середніми оцінками

# class Student:
#     def __init__(self, name, subjects ):
#         self.name = name
#         self.subjects = subjects
#
#     def add_new_subjects(self, subject_name, assessment_list):
#         if len(assessment_list) > 0:
#             self.subjects[subject_name] = assessment_list
#             print("Subject and assessments has been added")
#
#         else:
#             print("Assessments list is empty")
#
#     def delete_subject(self, subject_name):
#         if subject_name in self.subjects:
#             self.subjects.pop(subject_name)
#             print("Subject is removed")
#
#         else:
#             print("Subject not found")
#
#     def study_subject(self, subject_name):
#         random_value = random.randint(1, 100)
#         random_assessment = random.randint(3, 5)
#
#         if random_value > 20:
#             print(f"You have received a grade {random_assessment} for {subject_name}")
#             self.subjects[subject_name].append(random_assessment)
#
#     def get_avg_asses_for_subject(self, subject_name):
#         assessment_count = len(subject_name)
#         assessment_sum = sum(subject_name)
#         return  assessment_sum/assessment_count
#
#     def show_student_info(self):
#         print("Your info")
#         print(f"Name: {self.name}")
#         for keys, values in self.subjects.items():
#             sum_v = sum(values)
#             len_v = len(values)
#             print(f"Subject: {keys}, average assessment: {sum_v/len_v}")
#
# student1 = Student("Sasha", {"math":[4,4,5], "biology":[4,5,3]})
#
# student1.add_new_subjects("sub1", [3,3,3])
# student1.show_student_info()
# student1.study_subject("math")
# student1.show_student_info()

#=============================================================================================
# Завдання 5
# Створіть клас Магазин з атрибутами:
# назва
# заробіток
# словник з товарами, де ключ – назва товару, значення – кількість на складі
# словник з товарами, де ключ – назва товару, значення – ціна
# Додайте методи:
# вивід інформації: назва та список доступних товарів
# поповнення складу певним товаром(може бути новий)
# оформлення замовлення, якщо товар у достатній  кількості доступний

# class Shop:
#     def __init__(self, name, earnings, products_storage, products_prices):
#         self.name = name
#         self.earnings = earnings
#         self.products_storage = products_storage
#         self.products_prices = products_prices
#
#     def show_shop_info(self):
#         print("You can buy")
#         for product, price in self.products_prices.items():
#                     print(f"Product: {product}. Price: {price}.")
#
#     def add_product_to_storage(self, product_name, product_price, product_count):
#         if product_name in self.products_prices and product_name in self.products_storage:
#             self.products_prices[product_name] += product_price
#             self.products_storage[product_name] += product_count
#         else:
#             self.products_prices[product_name] = product_price
#             self.products_storage[product_name] = product_count
#
#     def do_order(self, product_name, product_count):
#         if product_name in self.products_storage and product_name in self.products_prices:
#             if self.products_storage[product_name] > 0:
#                 price = self.products_prices[product_name] * product_count
#                 self.products_storage[product_name] -= product_count
#                 print(f"You just bought {product_name}. Count: {product_count}. Price: {price}")
#             else:
#                 print("Count of product is lower than you want")
#
#
# shop1 = Shop("Best Shop", 10000, {"cola": 30, "fanta": 35,"apple":15},{"cola": 10, "fanta": 25,"apple":35})
# shop1.show_shop_info()
# shop1.add_product_to_storage("juice", 20, 5)
# shop1.show_shop_info()
# shop1.do_order("fanta", 5)