# Завдання 1
# Створіть абстрактний клас Character, атрибути
# name – ім’я
# max_hp – максимальний рівень здоров’я
# hp – нинішній рівень здоров’я
# level – рівень персонажа(від 1 до 20)
# intelligence – стат інтелекту
# strength – стат сили
# dexterity – стат спритності
# mana – стат мани
# defense – стат захисту
# Методи:
# attack() – абстрактний метод
# take_damage(damage) – отримує урон, зменшений на
# захист
# level_up() – збільшує рівень
# increase_stat(stat) – збільшує один з статів на 1
# rest() – відпочинок(відновлює hp до максимального)
# heal(heal_hp) – збільшує hp на heal_hp
import abc


class Character(abc.ABC):
    def __init__(self, name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.level = level
        self.intelligence = intelligence
        self.strength = strength
        self.dexterity = dexterity
        self.mana = mana
        self.defense = defense

    @abc.abstractmethod
    def attack(self):
        raise NotImplementedError("This method should be implemented")

    def take_damage(self, damage):
        damage_level = damage - self.defense
        if damage_level > 0:
            print(f"You took damage.")
            self.hp -= damage_level
            print(f"Your current HP: {self.hp}")
        else:
            print(f"You are not damaged")

    def level_up(self):
        self.level += 1
        print("You are leveled up")

    def increase_stat(self, stat):
        if stat == "intelligence":
            self.intelligence += 1
            print(f"You boosted your {stat}")

        elif stat == "strength":
            self.strength += 1
            print(f"You boosted your {stat}")

        elif stat == "dexterity":
            self.dexterity += 1
            print(f"You boosted your {stat}")

        elif stat == "mana":
            self.mana += 1
            print(f"You boosted your {stat}")

        elif stat == "defense":
            self.defense += 1
            print(f"You boosted your {stat}")

        else:
            raise ValueError("Wrong stat")

    def rest(self):
        self.hp = self.max_hp
        print("You use rest")

    def heal(self, heal_hp):
        self.hp += heal_hp

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print("You healed your HP")


# hero1 = Character("John", 100, 80, 3,80, 76, 50, 30, 25)
# hero1.take_damage(10)