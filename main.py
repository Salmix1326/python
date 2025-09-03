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

            if self.hp < 0:
                print("You are dead")

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


# Завдання 2
#============================================================================================================
# Створіть дочірній клас Paladin
# Методи:
# attack() – наносить 4*strength урону та зменшує mana на 5, якщо недостатньо, то наносить strength урону
# shield() – збільшує стат defense на 4+level
# unshield() – зменшує стат defense на 4+level
# heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana

class Paladin(Character):
    def attack(self):
        if self.mana >= 5:
            self.mana -= 5
            print(f"You are attacked with {self.strength * 4}")
            return self.strength * 4
        else:
            return self.strength

    def shield(self):
        self.defense += 4 + self.level
        print(f"Your defense is increased to {self.defense}")

    def unshield(self):
        self.defense -= 4 + self.level
        print(f"Your defense is decreased to {self.defense}")

    def heal_ally(self, ally: Character):
        heal_level = 5 + 2 * self.level + 0.5 * self.mana
        ally.heal(heal_level)
        print(f"{self.name} healed {ally.name}")


paladin1 = Paladin("Saint Knight", 100, 70,5, 95, 40, 20, 90, 45)
paladin2 = Paladin("Knight Of Trust", 100, 40,3, 87, 45, 40, 30, 15)
paladin1.heal_ally(paladin2)

# Завдання 3
#============================================================================================================
# Створіть дочірній клас Mage
# Методи:
# attack() – наносить 3*intelligence+4 урону та зменшує mana на 3, якщо недостатньо, то не наносить урону
# fireball() – наносить 2*intelligence+3 урону по області та зменшує mana на 5, якщо недостатньо, то не наносить урону
# heal_ally(ally) – лікує союзника на 3 + level + 3*intelligence

class Mage(Character):
    def attack(self):
        if self.mana >= 3:
            print(f"You is attacked with {3 * self.intelligence + 4} damage")
            self.mana -= 3
            return 3 * self.intelligence + 4
        else:
            return self.strength

    def fireball(self):
        if self.mana >= 5:
            print(f"You is attacked with {2 * self.intelligence + 3} damage")
            self.mana -= 5
            return 2 * self.intelligence + 3

        else:
            return self.strength

    def heal_ally(self, ally: Character):
        heal_level = 3 + self.level + 3 * self.intelligence
        ally.heal(heal_level)

    def rest(self):
        super().rest()
        self.mana += 10


# Завдання 4
#============================================================================================================
# Створіть дочірній клас Warrior
# Методи:
# attack() – наносить 4*strength+3 урону
# power_strike(enemies) – проходить по списку ворогів:
# якщо їхній рівень менший за рівень персонажа, то знищує його повністю

class Warrior(Character):
    def attack(self):
        print(f"You are attacked with {4 * self.strength + 3} damage")
        return 4 * self.strength + 3

    def power_strike(self, enemies: list):
        for enemy in enemies:
            if enemy.level < self.level:
                enemy.hp -= 0
                print(f"You killed {enemy.name}")


# Завдання 5
#============================================================================================================
# Створіть дочірній клас Rogue
# Методи:
# attack() – наносить strength+level урону

class Rogue(Character):
    def attack(self):
        print(f"You have inflicted {self.strength + self.level} damage")
        return self.strength + self.level
