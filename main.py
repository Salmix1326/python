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

class EnterNumber:
    def __init__(self):
        self.digits = LifoQueue()

    def add(self, digit: str):
        if digit.isdigit() and len(digit) == 1:
            self.digits.put(digit)
            print(f"{digit} is added to the list")

        else:
            print(f"This is not a number")

    def undo(self):
        if self.digits.empty():
            print("Number List is empty")
            return

        self.digits.get()
        print("You have delete the last num from the list")

    def get_number(self):
        number_str: str = ""

        while not self.digits.empty():
            number_str +=  self.digits.get()

        for digit in range(len(number_str)-1, -1, -1):
            self.digits.put(number_str[digit])

        return int(number_str[::-1])

    def clear(self):
        self.digits = LifoQueue()
        print("Number list is cleaned")


some_list = EnterNumber()

some_list.add("5")
some_list.add("9")
some_list.add("7")
some_list.add("1")

some_list.undo()
some_list.undo()

print(some_list.get_number())
print(some_list.get_number())