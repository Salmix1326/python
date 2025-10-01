# Завдання 1
#========================================================================================================
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
import os.path
import threading
#
#
# def maximum(nums, results: dict):
#     print("Функція maximum почала свою роботу.")
#     result = max(nums)
#     results["max"] = result
#     print("Функція maximum закінчила свою роботу.")
#
#
# def minimum(nums, results: dict):
#     print("Функція minimum почала свою роботу.")
#     result = min(nums)
#     results["min"] = result
#     print("Функція minimum закінчила свою роботу.")
#
#
# def get_nums():
#     nums = []
#     while True:
#         num = input("Введіть число зі списку або натисніть Enter: ")
#         if num == "":
#             return nums
#         nums.append(int(num))
#
#
# results_list = {}
# my_nums = get_nums()
#
# thread1 = threading.Thread(target=maximum, args=(my_nums, results_list))
# thread2 = threading.Thread(target=minimum, args=(my_nums, results_list))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(results_list)

# Завдання 2
#========================================================================================================
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки.
# Перший потік знаходить суму елементів у списку.
# Другий потік знаходить середнє арифметичне у списку.
# Результати обчислень виведіть на екран.

# def get_nums():
#     nums = []
#     while True:
#         num = input("Введіть число зі списку або натисніть Enter: ")
#         if num == "":
#             return nums
#         nums.append(int(num))
#
#
# def get_sum(nums: list, results: dict):
#     total_sum = 0
#     for num in nums:
#         total_sum += num
#
#     results["sum"] = total_sum
#
#     return results
#
#
# def get_avg(nums: list, results: dict):
#     total_sum = 0
#     for num in nums:
#         total_sum += num
#
#     avg_num = total_sum / len(nums)
#     results["avg"] = avg_num
#
#     return results
#
#
# result_list = {}
# my_nums = get_nums()
# thread1 = threading.Thread(target=get_sum, args=(my_nums, result_list))
# thread2 = threading.Thread(target=get_avg, args=(my_nums, result_list))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(result_list)

# Завдання 3
#========================================================================================================
# Користувач вводить з клавіатури шлях до файлу, що містить набір чисел.
# Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише парні елементи списку.
# Другий потік створює новий файл, в який запише лише непарні елементи списку.
# Кількість парних і непарних елементів виводиться на екран.
# import random
# import threading
# import json
# import os


# # nums = []
# #
# # for _ in range(1000000):
# #     random_num = random.randint(1, 100)
# #     nums.append(random_num)
# #
# #
# # with open("data/nums.json", "w") as file:
# #     json.dump(nums, file)


# def get_user_path():
#     while True:
#         file_path = input("Enter file path: ")
#
#         if not os.path.exists(file_path):
#             print("This file doesn't exist")
#             continue
#
#         if not file_path.endswith(".json"):
#             print("This is not JSON file")
#             continue
#
#         return file_path
#
#
# def get_even_nums(file_path):
#     print("Even start")
#
#     with open(file_path, 'r') as file:
#         nums = json.load(file)
#
#     even = []
#     for num in nums:
#         if num % 2 == 0:
#             even.append(num)
#
#     current_file_path = file_path[0:-5]
#     new_file_path = current_file_path + "_even.json"
#
#     directory, result = os.path.split(new_file_path)
#     directory = os.path.join(directory, "result")
#     os.mkdir(directory)
#     new_file_path = os.path.join(directory, result)
#
#     with open(new_file_path, 'w') as file:
#         json.dump(even, file)
#
#     print("Even end")
#
#
# def get_odd_nums(file_path):
#     print("Odd start")
#
#     with open(file_path, 'r') as file:
#         nums = json.load(file)
#
#     odd = []
#     for num in nums:
#         if num % 2 != 0:
#             odd.append(num)
#
#     current_file_path = file_path[0:-5]
#     new_file_path = current_file_path + "_odd.json"
#
#     directory, result = os.path.split(new_file_path)
#     os.mkdir(directory)
#     new_file_path = os.path.join(directory, result)
#
#     with open(new_file_path, 'w') as file:
#         json.dump(odd, file)
#
#     print("Odd end")
#
# file_path = get_user_path()
# thread1 = threading.Thread(target=get_even_nums, args=(file_path,))
# thread2 = threading.Thread(target=get_odd_nums, args=(file_path,))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()