# Завдання 1
# Створіть клас Pet з атрибутами
# name – ім’я тварини
# satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
# energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
# sleep() – збільшує energy до 100
# eat(food_amont) – їсть, збільшує satiety на food_amount
# play(activity_level) – абстрактний метод
# make_sound() – просто pass

# Створіть клас Cat
# Методи:
# play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
# make_sound() – виводить ‘Мяу’
# catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть

# Створіть клас Dog
# Методи:
# play(activity_level) – якщо satiety > 15, зменшує energy на acticity_level//2 та satiety на acticity_level//2
# make_sound() – виводить ‘Гав’
# fetch_ball() – ловить м’яча якщо satiety>10, зменшує energy на 5
import abc


class Pet(abc.ABC):
    def __init__(self, name, satiety = 50, energy = 50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
            self.energy = 100
            print(f"{self.name}'s energy level is up to 100")

    def eat(self, food_amount):
        if self.satiety + food_amount > 100:
            self.satiety = 100

        else:
            self.satiety += food_amount
        print(f"{self.name} satiety now is {self.satiety}")

    @abc.abstractmethod
    def play(self, activity_level):
        pass

    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            if self.energy >= 2 * activity_level and self.satiety >= activity_level:
                self.energy -= 2 * activity_level
                self.satiety -= activity_level

                print(f"{self.name} played. Energy: {self.energy}, Satiety: {self.satiety}")

            else:
                print("Not enough energy or satiety to play")

        else:
            print("Satiety is too low to play")

    def make_sound(self):
        print("Meow")

    def catch_mouse(self):
        if self.energy > 30:
            print(f"{self.name} caught a mouse")

            if self.satiety > 40:
                print(f"{self.name} plays with the mouse")

            else:
                print(f"{self.name} eats the mouse")

        else:
            print("Not enough energy to catch a mouse")


class Dog(Pet):
    def play(self,activity_level):
        if self.satiety > 15:
            if self.energy >= activity_level // 2 and self.satiety >= activity_level // 2:
                self.energy -= activity_level // 2
                self.satiety -= activity_level // 2

                print(f"{self.name} played. Energy: {self.energy}, Satiety: {self.satiety}")

            else:
                print("Energy or satiety is not enough to play")

        else:
            print("Satiety is not enough to play")

    def make_sound(self):
        print("Woof")

    def fetch_ball(self):
        if self.satiety > 10 and self.energy >= 5:
            self.energy -= 5

            print(f"{self.name} caught the ball. Energy level: {self.energy}")

        else:
            print("Satiety or energy is not enough to catch the ball")


cat1 = Cat("Tuzik", 50, 80)
dog1 = Dog("Barsik", 20, 50)

cat1.catch_mouse()
dog1.fetch_ball()
