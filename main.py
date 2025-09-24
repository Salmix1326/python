# Завдання 1
# Використовуючи бінарні дерева, організуйте роботу автопарку, де зберігаються автомобілі, відсортовані за маркою
#================================================================
# Клас Car
# Атрибути:
# brand – модель автомобіля
# model – марка автомобіля
# year – рік випуску
#================================================================
# Клас CarPark
# Атрибути:
# cars – дерево з автомобілями
# Методи:
# add(car) – добавити автомобіль
# remove(model) – видалити автомобіль
# search(model) – пошук автомобіля за маркою, якщо є то повертає автомобіь інакше None
# __len__() – кількість автомобілів
# sell_car(client, model) – продати автомобіль клієнту, якщо така марка присутня

import bintrees

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Brand: {self.brand}. Model: {self.model}. Year: {self.year}"


class CarPark:
    def __init__(self):
        self.cars = bintrees.AVLTree()

    def add(self, car: Car):
        self.cars[car.model] = car

    def remove(self, model: str):
        if model in self.cars:
            self.cars.pop(model)
            return

        print(f"No model {model} in car park found")

    def search(self, model):
        if model in self.cars:
            return self.cars[model]

        return None

    def __len__(self):
        return len(self.cars)

    def sell_car(self, client, model):
        if model in self.cars:
            print(f"{client} bought {model} from car park")
            self.cars.pop(model)
            return

        print(f"No {model} in car park found")


car1 = Car("Toyota", "Corolla", 2010)
car2 = Car("BMW", "X5", 2018)
car3 = Car("Tesla", "Model 3", 2022)
car4 = Car("Audi", "A4", 2015)
car5 = Car("Ford", "Mustang", 2020)

car_park = CarPark()

car_park.add(car1)
car_park.add(car2)
car_park.add(car3)
car_park.add(car4)
car_park.add(car5)

car_park.remove("Model 3")
car_park.remove("Inferno")

print(car_park.search("A4"))
print(car_park.search("Inferno"))

print(f"Count of cars in the park: {len(car_park)}")

car_park.sell_car("John", "A4")
car_park.sell_car("John", "A4")