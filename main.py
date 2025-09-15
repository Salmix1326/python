# Завдання 1
# ==================================================================================================================
# Використовуючи черги з пріоритетом створіть програму для симуляції роботи аеропорту.
# Кожен пасажир має пройти через 3 етапи: реєстрація, контроль безпеки, посадка.
# Відповідно аеропорт складається з 3-ох зон, кожна з яких має свою чергу.
# Коли Пасажир пройшов одну зону, то переходить в наступну.
# Пасажири з вищим пріоритетом обслуговуються першими
# ==================================================================
# Клас Zone – зона
# Атрибути:
# name – назва(реєстрація, контроль безпеки або посадка)
# passengers – черга пасажирів
# =====================
# Методи:
# add(passenger) – додає пацієнта в чергу з пріоритетом
# serve_passenger() – обслуговуємо наступного пасажира та повертає його
# ==================================================================
# Клас Airport – аеропорт
# Атрибути:
# zones – словник із зонами, ключем є назва зони
# passengers – список пасажирів, які успішно пройшли 3 зони
# =====================
# Методи:
# add(passenger) – додає пасажира в чергу на реєстрацію
# serve_registration() – обслуговує клієнта з черги реєстрації та переводить на котроль безпеки
# serve_security_control() – обслуговує клієнта з черги контролю безпеки та переводить на посадку
# serve_boarding() – обслуговує клієнта з черги посадки та переводить в passengers
# show_statistics() – вивести кількість пасажирів у кожній зоні та скільки успішно все пройшли
# ==================================================================
# Для цього скористайтесь класом Passenger
# Атрибути:
# name – ім’я
# priority – пріоритет

# Завдання 2
# ==================================================================================================================
# Створіть дочірні класи від Zone та перевизначте метод
# serve_passenger() щоб він повертав пару: пасажир та True/False в залежності від успішності перевірки.
# Перевірки:
# реєстрація – наявність білету(у багажі)
# безпека – відсутність небезпечних предметів у багажі: ніж, зброя, вибухівка
# посадка – перевірка не потрібна
from queue import PriorityQueue
import itertools


class Passenger:
    def __init__(self, name, priority, baggage=None):
        if baggage is None:
            baggage = []
        self.name = name
        self.priority = priority
        self.baggage = baggage


class Zone:
    _counter = itertools.count()

    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add(self, passenger):
        count = next(Zone._counter)
        self.passengers.put((passenger.priority, count, passenger))

    def serve_passenger(self):
        if self.passengers.empty():
            return None, False

        priority, count, passenger = self.passengers.get()
        print(f"{passenger.name} is checked in zone {self.name}")

        return passenger, True


class RegCheck(Zone):
    def serve_passenger(self):
        if self.passengers.empty():
            return None, False

        priority, count, passenger = self.passengers.get()

        if "ticket" in passenger.baggage:
            print(f"{passenger.name} passed registration")
            return passenger, True

        else:
            print(f"{passenger.name} failed registration (no ticket)")
            return passenger, False


class SecurityCheck(Zone):
    def serve_passenger(self):
        if self.passengers.empty():
            return None, False

        priority, count, passenger = self.passengers.get()

        if "knife" in passenger.baggage or "gun" in passenger.baggage or "explosives" in passenger.baggage:
            print(f"{passenger.name} failed security (dangerous item)")
            return passenger, False

        else:
            print(f"{passenger.name} passed security")
            return passenger, True


class BoardingZone(Zone):
    def serve_passenger(self):
        if self.passengers.empty():
            return None, False

        priority, count, passenger = self.passengers.get()

        print(f"{passenger.name} boarded the plane")

        return passenger, True


class Airport:
    def __init__(self):
        self.zones = {"registration": RegCheck("registration"), "security_control": SecurityCheck("security_control"),
                      "boarding": BoardingZone("boarding")}
        self.passengers = []
        self.failed_passengers = []

    def add(self, passenger: Passenger):
        self.zones["registration"].add(passenger)

    def serve_registration(self):
        passenger, check = self.zones["registration"].serve_passenger()

        if passenger is None:
            return

        if check:
            self.zones["security_control"].add(passenger)

        else:
            self.failed_passengers.append(passenger.name)

    def serve_security_control(self):
        passenger, check = self.zones["security_control"].serve_passenger()

        if passenger is None:
            return

        if check:
            self.zones["boarding"].add(passenger)

        else:
            self.failed_passengers.append(passenger.name)

    def serve_boarding(self):
        passenger, check = self.zones["boarding"].serve_passenger()

        if passenger is None:
            return

        if check:
            self.passengers.append(passenger.name)

        else:
            self.failed_passengers.append(passenger.name)

    def show_statistics(self):
        print("Airport statistics")
        print(f"Passengers in registration zone: {self.zones["registration"].passengers.qsize()}")
        print(f"Passengers in security_control zone: {self.zones["security_control"].passengers.qsize()}")
        print(f"Passengers in boarding zone: {self.zones["boarding"].passengers.qsize()}")
        print(f"Boarded passengers: {self.passengers}")
        print(f"Failed passengers: {self.failed_passengers}")


# # Використання
passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
passenger3 = Passenger("Charlie", 3, ["ticket"])
passenger4 = Passenger("David", 4, ["ticket", "laptop"])
passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
passenger6 = Passenger("Frank", 3, ["book"])
passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
passenger8 = Passenger("Hannah", 4, ["phone", "tablet"])
passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
passenger10 = Passenger("Jack", 1, ["ticket", "gun"])

# Створюємо аеропорт
airport = Airport()

# Додаємо пасажирів до реєстрації
airport.add(passenger1)
airport.add(passenger2)
airport.add(passenger3)
airport.add(passenger4)
airport.add(passenger5)
airport.add(passenger6)
airport.add(passenger7)
airport.add(passenger8)
airport.add(passenger9)
airport.add(passenger10)

# Проходимо етапи для кожного пасажира
for _ in range(10):
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

# Показуємо статистику
airport.show_statistics()