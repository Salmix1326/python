# Модуль 12. Структури даних
# Тема: Стеки. Частина 2
# Завдання 1
#============================================================================================
# Використовуючи стек створіть клас WebHistory
# Атрибути:
# history – стек з історією відвідування веб сторінок
# forward_history – стек з веб сторінками, для повернення «вперед»
# Методи:
# add(page) – перейти на нову сторінку
# undo() – повернутись на попередню сторінку
# redo() – перейти вперед
# get_current_page() – повернути поточну сторінку
from queue import LifoQueue


# class WebHistory:
#     def __init__(self, history, forward_history):
#         self.history = LifoQueue()
#         self.forward_history = LifoQueue()
#
#     def add(self,page):
#         self.history.put(page)
#         self.forward_history = LifoQueue()
#         print(f"You enter the {page}")
#
#     def undo(self):
#         if self.forward_history.empty():
#             print("Your history is empty")
#             return
#
#         page = self.history.get()
#         self.forward_history.put(page)
#
#         if self.history.empty():
#             print("Your history is empty")
#
#         page = self.history.queue[-1]
#         print(f"You return to the {page}")
#
#     def redo(self):
#         if self.forward_history.empty():
#             print("Your redo history is empty")
#             return
#
#         page = self.forward_history.get()
#         self.history.put(page)
#
#         if self.forward_history.empty():
#             print("Your redo history is empty")
#
#         page = self.forward_history.queue[-1]
#         print(f"You return to the {page}")
#
#
# help(LifoQueue)

# Завдання 2
# #============================================================================================
# Використовуючи стек створіть клас EnterNumber для введення числа в рядку
# Атрибути:
# digits – стек з введеними цифрами
# Методи:
# add(digit) – додати нову цифру, вивести помилку якщо не цифра
# undo() – видалити останню цифру
# get_number() – повернути число
# clear() – очистити стек

# class EnterNumber:
#     def __init__(self):
#         self.digits = LifoQueue()
#
#     def add(self, digit: str):
#         if digit.isdigit() and len(digit) == 1:
#             self.digits.put(digit)
#             print(f"{digit} is added to the list")
#
#         else:
#             print(f"This is not a number")
#
#     def undo(self):
#         if self.digits.empty():
#             print("Number List is empty")
#             return
#
#         self.digits.get()
#         print("You have delete the last num from the list")
#
#     def get_number(self):
#         number_str: str = ""
#
#         while not self.digits.empty():
#             number_str +=  self.digits.get()
#
#         for digit in range(len(number_str)-1, -1, -1):
#             self.digits.put(number_str[digit])
#
#         return int(number_str[::-1])
#
#     def clear(self):
#         self.digits = LifoQueue()
#         print("Number list is cleaned")
#
#
# some_list = EnterNumber()
#
# some_list.add("5")
# some_list.add("9")
# some_list.add("7")
# some_list.add("1")
#
# some_list.undo()
# some_list.undo()
#
# print(some_list.get_number())
# print(some_list.get_number())

# Завдання 3
#============================================================================================
# Використовуючи стек створіть клас Calculator
# Атрибути:
# operation – тип операції(за замовчуванням None)
# answers – стек з результатами(за замовчуванням там один 0)
# Методи:
# read() – читає текст введений користувачем, далі виконує наступні дії, в залежності від тексту
# операція(+-*/) – змінює operation
# число – дістати останнє число з answers(не видаляючи) та виконати дію operation, результа вивести на екран та добавити в answers
# слово “show” – показати останній результат
# слово «undo» -- повернутись до попереднього результату
# from queue import LifoQueue
#
#
# class Calculator:
#     def __init__(self):
#         self.operation = None
#         self.answers = LifoQueue()
#         self.answers.put(0)
#
#     def read(self):
#         while True:
#             user_choice = input("Enter command: ")
#
#             if user_choice == "+":
#                 self.operation = "+"
#                 print("Operation type is \"+\"")
#
#             elif user_choice == "-":
#                 self.operation = "-"
#                 print("Operation type is \"-\"")
#
#             elif user_choice == "/":
#                 self.operation = "/"
#                 print("Operation type is \"/\"")
#
#             elif user_choice == "*":
#                 self.operation = "*"
#                 print("Operation type is \"*\"")
#
#             elif user_choice == "number":
#                 user_num = int(input("Enter number: "))
#                 last_num = self.answers.get()
#                 self.answers.put(last_num)
#
#                 if self.operation is not None:
#                     if self.operation == "+":
#                         res = user_num + last_num
#                         print(self.answers)
#                         self.answers.put(res)
#
#                     elif self.operation == "-":
#                         res = user_num - last_num
#                         self.answers.put(res)
#
#                     elif self.operation == "/":
#                         res = user_num / last_num
#                         self.answers.put(res)
#
#                     elif self.operation == "*":
#                         res = user_num * last_num
#                         self.answers.put(res)
#
#             elif user_choice == "show":
#                 last_num = self.answers.get()
#                 print(f"Last result: {last_num}")
#                 self.answers.put(last_num)
#
#             elif user_choice == "undo":
#                 if self.answers.empty():
#                     print("Results history is empty")
#                     return
#
#                 self.answers.get()
#
#                 print("You returned to previous result")
#
#             elif user_choice == "exit":
#                 break
#
#
# calc = Calculator()
# calc.read()


# Завдання 4
#============================================================================================
# Є вираз з дужками, за допомогою стеків визначіть чи правильно розтавлені дужки, якщо ні то виведіть індекс «проблемної» дужки.

# text = ("def highlight_character(text, ind): for i, char in enumerate(text, start=1): if i == ind: print(f[0m"", end="") else print(char, end="") print()")
#
# def correct_method(expr):
#     RED = "\033[91m"
#     RESET = "\033[0m"
#
#     stack = LifoQueue()
#
#     for i, char in enumerate(expr):
#         if char in "([{":
#             stack.put((i, char))
#
#         elif char in ")]}":
#             if stack.empty():
#                 print(expr[:i] + f"{RED}{char}{RESET}" + expr[i+1:])
#                 print('Brackets is not correct')
#                 return
#
#             j, last_bracket = stack.get()
#
#             if last_bracket + char not in ['()', '{}', '[]']:
#                 print(expr[:j] + f"{RED}{last_bracket}{RESET}" + expr[j + 1:i] + f"{RED}{char}{RESET}" + expr[i+1:])
#                 print('Brackets is not correct')
#                 return
#
#     if not stack.empty():
#         i, char = stack.get()
#         print(expr[:i] + f"{RED}{char}{RESET}" + expr[i + 1:])
#         print('Too many open brackets')
#         return
#
#     print('Brackets is correct')
#
# correct_method(text)

