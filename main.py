# Завдання 1
# Створіть клас Message з атрибутами
# user – ім’я автора повідомлення
# text – текст повідомлення
# time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
# __str__(self) – повертає текст повідомлення та час
# __len__(self) – повертає довжину повідомлення
# __gt__(self, other) – перевіряє чи є повідомлення self старішим за other
# Створіть список з декількома повідомленнями та виведіть його. Відсортуйте список і знову виведіть
import datetime


class Message:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.time = datetime.datetime.now()

    def __str__(self):
        return f"Time now: {self.time.strftime('%H:%M')}. User: {self.user}"

    def __len__(self):
        return len(self.text)

    def __gt__(self, other):
        return self.time > other.time

m1 = Message("Sasha", "Hi There")
m2 = Message("John", "I'm John")
m3 = Message("Mike", "Good Morning!")

message_list = [m2, m1, m3]
message_list.sort()

for message in message_list:
        print(message)

#============================================================================================
# Завдання 2
# Створіть клас Song з атрибутами
# name – назва пісні
# author – ім’я автора
# методи:
# __eq__(self, other) – перевіряє чи дві пісні однакові
# __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
# songs – список пісень(об’єкти класу Song)
# методи:
# __len__(self) – повертає кількість пісень
# __contains__(self, item) – перевіряє чи є пісня в плейлисті
# __iter__(self) – повертає літератор для циклу for
# add_song(self, song) – додає пісню в плейлист
# remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну пісню на екран

class Song:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"Song title: {self.name}. Author name: {self.author}"


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __contains__(self, song):
        return song in self.songs

    def __iter__(self):
        return iter(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.pop(song)


song1 = Song("Imagine", "John Lennon")
song2 = Song("Bohemian Rhapsody", "Queen")
song3 = Song("Shape of You", "Ed Sheeran")

song_list = [song1, song2, song3]

playlist1 = Playlist(song_list)

for song in playlist1:
    print(song)

# Завдання 3
# #============================================================================================
# Створіть клас Cart з атрибутами
# items – список товарів
# total – загальна ціна товарів
# методи:
# __str__(self) – повертає рядок зі списком товарів
# __len__(self) – повертає кількість товарів
# __add__(self, other) – об’єднує 2 кошики та повертає новий кошик
# Створіть два кошики.
# Виведіть кількість товарів в кожному з них.
# Виведіть самі кошики.
# Об’єднайте їх та виведіть кількість товарів в новому кошику та товари в ньому

class Cart:
    def __init__(self, items, total):
        self.items = items
        self.total = total

    def __str__(self):
        return  f"Items: {self.items}"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return self.items.extend(other.generator())

    def generator(self):
        for item in self.items:
            yield item


products1 = ["apple", "peach", "banana"]
products2 = ["coffee", "tea", "juice"]

cart1 = Cart(products1, 500)
cart2 = Cart(products2, 400)

print(cart1)
print(cart2)
print(len(cart1))
print(len(cart2))

cart1.__add__(cart2)

print(cart1)
print(f"{cart1}. Len: {len(cart1)}")