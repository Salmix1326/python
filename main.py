# Завдання 1
# Створіть клас Recipe з атрибутами
# name – назва страви
# ingredients – список продуктів
# text – текст рецепту
# time – час приготування
# методи:
# __str__(self) – повертає назву страви
# __contains__(self, item) – перевіряє чи є інгредієнт в рецепті
# __gt__(self, other) – перевіряє чи є час приготування self більшим за other
# display_info(self) – виводить всю інформацію про рецепт

class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time

    def __str__(self):
        return f"Dish name: {self.name}"

    def __contains__(self, ingredient):
        return ingredient in self.ingredients

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        return (f"Dish name: {self.name}. Dish ingredients: {self.ingredients}. "
                f"Dish recipe: {self.text}. Cooking time: {self.time} min")


# Створіть декілька рецептів та добавте їх у список.
dish1 = Recipe("Піца",
 ["борошно", "вода", "дріжджі", "томат", "сир"],
 "Готуємо тісто, додаємо інгредієнти та запікаємо",
 30)
dish2 =  Recipe("Салат",
 ["томат", "огірок", "зелень", "олія"],
 "Нарізаємо овочі, додаємо зелень та поливаємо олією",
 10)
dish3 = Recipe("Суп",
 ["вода", "картопля", "морква", "м'ясо"],
 "Варимо всі інгредієнти до готовності",
 45)

dish_list = [dish1, dish2, dish3]

# Виведіть назви тих рецептів, які містять інгредієнт томат
print(f"Dishes with tomato ingredient:")
for dish in dish_list:
    if "томат" in dish:
        print(dish)

# Виведіть повну інформацію рецепта з найменшим часом приготування, скористайтесь функцією min
min_dish_time = min(dish_list)
print(f"Fastest dish recipe - {min_dish_time.name}: {min_dish_time.text}")