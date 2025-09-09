# Завдання 1
#=======================================================================================================
# Створіть клас Passenger з атрибутами
# name – ім’я
# destination – місце, куди прямує
#=======================================================================================================
# Створіть клас Transport з атрибутами
# speed – швидкість
# Методи
# move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали
#=======================================================================================================
# Створіть клас Bus з атрибутами
# passengers – список пасажирів(об’єкти класу Passenger)
# capacity – максимальна можлива кількість пасажирів
# Методи
# board_passenger(passenger) – якщо є місце, додає
# пасажира
# move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну кількість) та викликає батьківський метод move()


class Passenger:
    def __init__(self, name, destination, distance_to_stop):
        self.name = name
        self.destination = destination
        self.distance_to_stop = distance_to_stop


class Transport:
    def __init__(self, speed, final_destination):
        self.speed = speed
        self.final_destination = final_destination
        self.traveled_distance = 0

    def move(self, destination, distance):
        self.traveled_distance += distance
        time = self.traveled_distance / self.speed

        if destination != self.final_destination:
            print(f"Transport moved to {destination}. "
                  f"Distance: {distance} km. "
                  f"Total traveled: {self.traveled_distance} km. "
                  f"Travel time: {time:.2f} hours. "
                  f"Final destination: {self.final_destination}")

        else:
            print(f"Transport moved to final destination \"{self.final_destination}\". Distance: {distance} km. "
                  f"Total traveled: {self.traveled_distance} km. "
                  f"Travel time: {time:.2f} hours")


class Bus(Transport):
    def __init__(self, speed, final_destination, capacity, passengers=None):
        super().__init__(speed, final_destination)

        self.passengers = passengers if passengers else []
        self.capacity = capacity

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)

            print(f"{passenger.name} boarded the bus.")

        else:
            print("The bus is full!")

    def stop(self, destination, absolute_stop_distance):
        leaving_passengers = [p for p in self.passengers if p.destination == destination]

        distance = absolute_stop_distance - self.traveled_distance

        for p in leaving_passengers:
            self.passengers.remove(p)

        print(f"{len(leaving_passengers)} passengers got off at {destination}.")

        super().move(destination, distance)


passenger1 = Passenger("Iron Man", "New York", 50)
passenger2 = Passenger("Avatar", "Pandora", 100)
passenger3 = Passenger("Legolas", "Rivendell", 2000)
passengers_list = [passenger1, passenger2, passenger3]

bus1 = Bus(100, "Mordor", 50, passengers_list)

passenger4 = Passenger("Gendalf", "Mordor", 5000)
bus1.board_passenger(passenger4)

bus1.stop("New York", 50)
bus1.stop("Pandora", 100)
bus1.stop("Rivendell", 2000)

bus1.stop("Mordor", 5000)