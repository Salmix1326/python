# Завдання 1
#==================================================================================================================
# Використовуючи чергу створіть клас FastFoodQueue для організації роботи черг у фасфуді.
# Є 4 каси, новий клієнт стає в ту, де найменше людей.
# Коли клієнт зробив замовлення, його добавляють в чергу на отримання.
# Має зберігатися час, коли людина зробила замовлення, та коли отримала замовлення.
# Інформація про час обслуговування має зберігатись у окремому списку
#==================================================================================================================
# Атрибути:
# queues – список з 4-ма чергами до кас
# order_queue – черга клієнтів на отримання замовлення
# service_duration_history – список з часом обслуговування клієнтів
#==================================================================================================================
# Методи:
# add(client) – додає клієнта в найкоротшу чергу
# serve(idx) – обслуговуємо клієнта з черги за індексом.
# Треба додати клієнта в order_queue разом з часом коли зроблено замовлення
# make_order() – видає готове замовлення клієнту  та обраховує скільки часу очікував клієнт.
# Це число треба добавити в service_duration_history
# show_statistics() – виводить мінімальний, максимальний та середній час обслуговування клієнтів
from queue import Queue
import time


class Client:
    def __init__(self, name):
        self.name = name
        self.time = time.time()


class FastFoodQueue:
    def __init__(self):
        self.queues = [Queue(), Queue(), Queue(), Queue()]
        self.order_queue = Queue()
        self.service_duration_history = []

    def add(self, client_name):
        min_queue_len = min(self.queues, key= lambda item: item.qsize())
        min_queue_len.put(client_name)

    def serve(self, idx):
        if self.queues[idx].empty():
            print("This queue is empty")
            return

        client_name = self.queues[idx].get()
        client = Client(client_name)
        self.order_queue.put(client)

        print(f"{client.name} is served")

    def make_order(self):
        client = self.order_queue.get()
        print(f"{client.name} receive order")

        current_time = time.time()
        order_time = current_time - client.time

        self.service_duration_history.append(order_time)

    def show_statistics(self):
        min_time = min(self.service_duration_history)
        max_time = max(self.service_duration_history)
        avg_time = sum(self.service_duration_history) / len(self.service_duration_history)

        print(f"Min time: {min_time}.\nMax time: {max_time}.\nAverage time: {avg_time}")


# Тестування
fast_food = FastFoodQueue()
fast_food.add("Олег")
fast_food.add("Анна")
fast_food.add("Марія")
fast_food.add("Сергій")

fast_food.serve(0)
fast_food.serve(1)

time.sleep(2)
fast_food.make_order()
time.sleep(3)
fast_food.make_order()

fast_food.show_statistics()


# # TASK 2
# class Passenger:
#     def __init__(self, name, priority):
#         self.name = name
#         self.priority = priority
#
#
# class Zone:
#     pass
#
#
# class Airport:
#     pass
#
#
# # Тестування
# airport = Airport()
# passengers = [
#     Passenger("Олег", 3),
#     Passenger("Анна", 1),
#     Passenger("Марія", 4),
#     Passenger("Сергій", 2)
# ]
#
# for p in passengers:
#     airport.add(p)
#
# airport.serve_registration()
# airport.serve_registration()
# airport.serve_security_control()
# airport.serve_boarding()
#
# airport.show_statistics()
#
#
# # TASK3
# class Passenger:
#     def __init__(self, name, priority, baggage=None):
#         if baggage is None:
#             baggage = []
#         self.name = name
#         self.priority = priority
#         self.baggage = baggage
#
#
# # Використання
# passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
# passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
# passenger3 = Passenger("Charlie", 3, ["ticket"])
# passenger4 = Passenger("David", 4, ["ticket", "laptop"])
# passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
# passenger6 = Passenger("Frank", 3, ["book"])
# passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
# passenger8 = Passenger("Hannah", 5, ["phone", "tablet"])
# passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
# passenger10 = Passenger("Jack", 1, ["ticket", "gun"])
#
# # Створюємо аеропорт
# airport = Airport()
#
# # Додаємо пасажирів до реєстрації
# airport.add(passenger1)
# airport.add(passenger2)
# airport.add(passenger3)
# airport.add(passenger4)
# airport.add(passenger5)
# airport.add(passenger6)
# airport.add(passenger7)
# airport.add(passenger8)
# airport.add(passenger9)
# airport.add(passenger10)
#
# # Проходимо етапи для кожного пасажира
# for _ in range(10):
#     airport.serve_registration()
#     airport.serve_security_control()
#     airport.serve_boarding()
#
# # Показуємо статистику
# airport.show_statistics()