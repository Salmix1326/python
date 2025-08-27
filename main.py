# Завдання 1
#===========================================================================================
# Створіть наступні класи:
# Rectangle – атрибути width, height
# Circle – атрибути radius
# Triangle – атрибути a, b, c
# Методи:
# get_perimeter()
# display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи.

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_perimeter(self):
#         perimeter  = 2 * ( self.width + self.height)
#         return perimeter
#
#     def display_info(self):
#         print("Это прямоугольник")
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_perimeter(self):
#         perimeter  = 2 * 3.14 * self.radius
#         return perimeter
#
#     def display_info(self):
#         print("Это круг")
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         perimeter  = self.a + self.b + self.c
#         return perimeter
#
#     def display_info(self):
#         print("Это треугольник")
#
#
# def create_figure():
#     user_choice = input("Выберите фигуру прямоугольник, круг, треугольник: ")
#
#     if user_choice == "прямоугольник":
#         width = int(input("Введите ширину: "))
#         height = int(input("Введите длинну: "))
#         rectangle = Rectangle(width, height)
#         print(f"Периметр прямоугольника - {rectangle.get_perimeter()}")
#
#     elif user_choice == "круг":
#         radius = int(input("Введите радиус: "))
#         circle = Circle(radius)
#         print(f"Периметр круга - {circle.get_perimeter()}")
#
#     elif user_choice == "треугольник":
#         a = int(input("Введите сторону A: "))
#         b = int(input("Введите сторону B: "))
#         c = int(input("Введите сторону C: "))
#         triangle = Triangle(a, b, c)
#         print(f"Периметр треугольника - {triangle.get_perimeter()}")
#
# create_figure()
#
# rectangle1 = Rectangle(20, 30)
# rectangle2 = Rectangle(10, 15)
# rectangle3 = Rectangle(18, 9)
#
# circle1 = Circle(20)
# circle2 = Circle(10)
# circle3 = Circle(15)
#
# triangle1 = Triangle(1, 2, 3)
# triangle2 = Triangle(5, 6, 8)
# triangle3 = Triangle(11, 5, 2)
#
# figures = [rectangle1, rectangle2, rectangle3, circle1, circle2, circle3, triangle1, triangle2, triangle3]
#
# for figure in figures:
#     print(f"Perimeter of this figure: {figure.get_perimeter()}")

# Завдання 2
# ===========================================================================================
# Створіть наступні класи:
# Manager – атрибути name, base_salary
# Developer – атрибути name, base_salary, work_experience
# Inter – атрибути name, base_salary
# Методи:
# get_salary() – менеджер отримує базову ставку,
# розробник отримує на 20% більше якщо стаж більше 4 років,
# інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у користувача тип працівника та потрібні атрибути і повертає об’єкт.
# Створіть декілька співробітників, добавте їх у список та для кожного викличте відповідні методи.

# class Manager:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary
#
#     def get_salary(self):
#         return self.base_salary
#
#
# class Developer:
#     def __init__(self, name, base_salary, work_experience):
#         self.name = name
#         self.base_salary = base_salary
#         self.work_experience = work_experience
#
#     def get_salary(self):
#         if self.work_experience > 4:
#             return self.base_salary + self.base_salary * 0.2
#
#         else:
#             return self.base_salary
#
#
# class Inter:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary
#
#     def get_salary(self):
#         return self.base_salary / 2
#
#
# def create_worker():
#     user_choice = int(input("Enter your position in company - manager(1), developer(2), inter(3): "))
#     user_name = input("Enter your name: ")
#     user_salary = int(input("Enter your salary: "))
#
#     if user_choice == 1:
#         manager1 = Manager(user_name, user_salary)
#         print(f"{user_name}, your salary is {manager1.get_salary()}")
#         return manager1
#
#
#     if user_choice == 2:
#         user_experience = int(input("Enter your experience: "))
#         developer1 = Developer(user_name, user_salary, user_experience)
#
#         print(f"{user_name}, your salary is {developer1.get_salary()}")
#         return developer1
#
#     if user_choice == 3:
#         inter1 = Inter(user_name, user_salary)
#
#         print(f"{user_name}, your salary is {inter1.get_salary()}")
#         return inter1
#
# workers = []
#
# count = 3
# while count !=0:
#     new_worker = create_worker()
#     workers.append(new_worker)
#     count -= 1
#
# for worker in workers:
#     print(type(worker))
#     print(f"Salary: {worker.get_salary()}")

# Завдання 3
# ===========================================================================================
# Створіть наступні класи:
# Car – атрибути speed
# Bicycle – атрибути speed
# Boat – атрибути speed
# Методи:
# move() – виводить повідомлення про рух
# Car – їде по шосе зі швидкістю
# Bicycle – їде по дорозі зі швидкістю
# Boat – пливе по воді зі швидкістю
# check_speed(speed) – перевіряє чи правильна швидкість,
# якщо ні то в __init__ треба викикати ValueError з відповідним повідомленням
# Car – від 20 до 200
# Bicycle – від 10 до 30
# Boat – від 0 до 50
# Напишіть функцію create_vehicle() яка запитує у користувача тип транспорту та потрібні атрибути і повертає об’єкт.
# Створіть декілька транспортних засобів, добавте їх у список та для кожної викличте відповідні методи.

# class Car:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def move(self):
#         print(f"Car is gonna highway with {self.speed} km/h")
#
#     def check_speed(self):
#         if 200 >= self.speed >= 20:
#             return "Speed is OK"
#
#         else:
#             return "Unacceptable speed"
#
#
# class Bicycle:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def move(self):
#         print(f"Bicycle is gonna road with {self.speed} km/h")
#
#     def check_speed(self):
#         if 30 >= self.speed >= 10:
#             return "Speed is OK"
#
#         else:
#             return "Unacceptable speed"
#
# class Boat:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def move(self):
#         print(f"Boat is sailing with {self.speed} km/h")
#
#     def check_speed(self):
#         if 50 >= self.speed >= 0:
#             return "Speed is OK"
#
#         else:
#             return "Unacceptable speed"
#
#
# def create_vehicle():
#     user_choice = int(input("Enter your vehicle type - car(1), bicycle(2), boat(3): "))
#
#     if user_choice == 1:
#         try:
#             user_speed = int(input("Enter your speed: "))
#
#             if 200 >= user_speed >= 20:
#                 car = Car(user_speed)
#                 car.check_speed()
#
#             else: raise ValueError
#
#         except ValueError:
#             print("Unacceptable speed")
#
#     if user_choice == 2:
#         try:
#             user_speed = int(input("Enter your speed: "))
#
#             if 30 >= user_speed >= 10:
#                 car = Car(user_speed)
#                 car.check_speed()
#
#             else: raise ValueError
#
#         except ValueError:
#             print("Unacceptable speed")
#
#     if user_choice == 3:
#         try:
#             user_speed = int(input("Enter your speed: "))
#
#             if 50 >= user_speed >= 0:
#                 car = Car(user_speed)
#                 car.check_speed()
#
#             else: raise ValueError
#
#         except ValueError:
#             print("Unacceptable speed")
#
# create_vehicle()
#
# car1 = Car(190)
# car2 = Car(250)
# bicycle1 = Bicycle(35)
# bicycle2 = Bicycle(20)
# boat1 = Boat(60)
# boat2 = Boat(20)
#
# vehicles = [car1, car2, bicycle1, bicycle2, boat1, boat2]
#
# for vehicle in vehicles:
#     print(f"{type(vehicle)}. Speed: {vehicle.speed}. {vehicle.check_speed()}")

# Завдання 4. Квестова гра
# ===========================================================================================
# Створіть наступні класи:
# Warrior – атрибути name, health, attack
# Mage – атрибути name, health, mana
# Archer – атрибути name, health, arrows
# Методи:
# attack() – виводить повідомлення про атаку (залежно від типу героя)
# is_alive() – перевіряє, чи здоров’я > 0
# Напишіть функцію create_hero(), яка запитує у користувача тип героя та його характеристики і повертає об’єкт.
# Створіть команду героїв, добавте у список і змусьте їх зробити кілька дій.

class Warrior:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack(self):
        print(f"{self.name} is attacking with sword and shield")

    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} is alive and ready for attack")


class Mage:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack(self):
        print(f"{self.name} is attacking with fire spell")

    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} is alive and ready for attack")


class Archer:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack(self):
        print(f"{self.name} is attacking with bow")

    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} is alive and ready for attack")


def create_hero():
    user_hero_class_choice = int(input("Choose your hero class: warrior(1), mage(2), archer(3): "))

    if user_hero_class_choice == 1:
        try:
            user_name = input("Enter your name: ")
            warrior = Warrior(user_name, 100,20)
            warrior.attack()

        except ValueError:
            print("Unacceptable speed")

    if user_hero_class_choice == 2:
        try:
            user_name = input("Enter your name: ")
            mage = Mage(user_name, 100, 20)
            mage.attack()

        except ValueError:
            print("Unacceptable speed")

    if user_hero_class_choice == 3:
        try:
            user_name = input("Enter your name: ")
            archer = Archer(user_name, 100, 20)
            archer.attack()

        except ValueError:
            print("Unacceptable speed")


create_hero()