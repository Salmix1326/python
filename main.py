# Завдання 1
#===================================================================================================
# Напишіть гру вгадати число: комп’ютер загадує число від 1 до 100.
# Користувач вводить свої відповіді на що отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
# почати нову гру – користувач вводить числа до правильної відповіді
# вивести результат – кількість перемог та програшів
# зберегти дані – зберегти кількості перемог та програшів у файл
# завантажити дані – завантажити кількості перемог та програшів
# Реалізуйте все функціями
import json
import random


class Game:
    def __init__(self): # инициализация
        self.games_count = 0
        self.wins = 0
        self.defeats = 0

    def start_game(self):
        comp_num = random.randint(1, 100) # настройки перед игрой
        counter = 5
        self.games_count += 1

        while counter != 0:
            try:
                print(f"You have {counter} tries")
                user_num = input("Enter your number 1-100: ") # ввод
                print()

                test_str = user_num
                user_num_check = int(user_num)

                # разные проверки на ввод числа
                if len(test_str) > 2:
                    print("You must enter max 2 digits")
                    print()
                    continue

                if user_num_check < 0 or user_num_check > 100:
                    print("You must enter number 1-100")
                    print()
                    continue

                if not test_str.isdigit():
                    print("You must print a number")
                    print()
                    continue

                if len(test_str) == 2 and test_str[0] == "0":
                    print("You entered 2 digits and first digit is 0. It is wrong number")
                    print()
                    continue

                # логика побед/поражений
                if user_num_check == comp_num:
                    print("You guessed number!")
                    print()

                    self.wins += 1
                    return

                else:
                    print("Your number is wrong")
                    print()

                    if user_num_check > comp_num:
                        print("Computer's num is lower")
                        print()
                    else:
                        print("Computer's num is greater")
                        print()

                counter -= 1

            except ValueError:
                print("You must enter a number")
                print()

        print(f"You spend all your tries. Computer num was: {comp_num}. You defeat.")
        print()

        self.defeats += 1

    def games_info(self): # вывод статистики
        print(f"Games statistics")
        print(f"Games: {self.games_count}. Wins: {self.wins}. Defeats: {self.defeats}")
        print()

    # работа с файлами
    def save_data(self):
        data_dict = {
            "games": self.games_count,
            "wins": self.wins,
            "defeats": self.defeats
        }

        with open("games_data", "w", encoding="utf-8") as file:
            json.dump(data_dict, file, indent=4)

    def load_data(self):
        with open("games_data", "r", encoding="utf-8") as file:
            games_data = json.load(file)

            return games_data


# тесты
game = Game()
game.start_game()
game.save_data()
game.games_info()