# Курс: «AI + Python
# Підведення підсумків. Іспит
# Частина 1: Основи Python
#============================================================================================================
# 1. Напишіть програму, яка приймає два цілих числа від користувача і виводить суму діапазону чисел між ними.
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
total_sum = 0

for num in range(num1, num2 + 1):
    total_sum += num

print(f"Total sum: {total_sum}")

# 2. Напишіть програму, для знаходження суми всіх парних чисел від 1 до 100.
total_sum = 0

for num in range(1, 100 + 1):
    if num % 2 == 0:
        total_sum += num

print(f"Total sum for even numbers: {total_sum}")

# 3. Напишіть програму, яка приймає рядок від користувача і виводить кожну літеру рядка на окремому рядку.
user_word = input("Type your string: ")

for char in user_word:
    print(char)

# 4. Напишіть програму, яка створює список цілих чисел та виводить новий список, який містить лише парні числа з вихідного списку.
random_nums = [num for num in range(1, 30)]
even_nums = []

for num in random_nums:
    if num % 2 == 0:
        even_nums.append(num)

print(f"Even numbers: {even_nums}")

# 5. Напишіть функцію, яка приймає список рядків від користувача і повертає новий список,
# що містить лише рядки, що починаються з великої літери.
def get_uppercase_word(string_list):
    res_list = []

    for string in string_list:
        if string[0].isupper():
            res_list.append(string)

    return res_list

string_list = []

while True:
    user_string = input("Enter some string or enter END: ")

    if user_string == "END":
        break

    string_list.append(user_string)

print(f"Only strings with first upper letter: {get_uppercase_word(string_list)}")

# 6. Напишіть функцію, яка приймає список рядків від користувача і повертає новий список, що містить лише рядки, які містять слово "Python".
def get_stings_with_python_word(string_list):
    res_list = []

    for string in string_list:
        if "Python" in string:
            res_list.append(string)

    return res_list

string_list = []

while True:
    user_string = input("Enter some string or enter END: ")

    if user_string == "END":
        break

    string_list.append(user_string)

print(f"Only string with Python word: {get_stings_with_python_word(string_list)}")

# 7. (додаткове на кристалики). Напишіть програму, яка створює словник, де ключами є слова, а значеннями - їхні визначення.
# Дозвольте користувачу додавати, видаляти та шукати слова у цьому словнику.
data = {
    "num1": 10,
    "some_word": "apple",
    "some_list": [1, 2, 4]
}

def add_data():
    user_key = input("Enter word to add: ")
    user_value = input("Enter value to add: ")

    if user_key in data:
        print("This word is in dataset already")
        return

    data[user_key] = user_value
    print("Word has been added")


def delete_data():
    user_key = input("Enter word to delete: ")

    if not user_key in data:
        print("This word isn't in dataset")
        return

    data.pop(user_key)
    print("Word has been deleted")


def search_data():
    user_key = input("Enter word for search: ")

    if not user_key in data:
        print("This word isn't in dataset")
        return

    print(f"Word: {user_key}. Word value: {data[user_key]}")


add_data()
delete_data()
search_data()
print(data)

# 8. (додаткове на кристалики)
# Використовуючи лямбда-функцію, напишіть вираз, який сортує список кортежів за другим елементом кожного кортежу
# (наприклад, [(1, 3), (3, 2), (2, 1)]).

nums = [(1, 8), (4, 2), (1, 1)]

result = sorted(nums, key=lambda x: x[1])

print(list(result))

# Частина 2: Об'єктно-орієнтоване програмування (ООП)
#============================================================================================================
# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення інформації про сайт.
#==========================================================
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
#==========================================================
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з певною назвою та URL.
# Додайте можливість створювати нові сторінки для сайту, вводячи заголовок та вміст.
# Реалізуйте функцію для видалення сторінок з сайту.
# Включіть функцію для відображення всієї інформації про сайт, включаючи список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з користувачем.
# Користувач повинен мати змогу вибирати дії, такі як створення сайту, додавання/видалення сторінок, перегляд інформації про сайт.

# Додаткові можливості (за бажанням на кристалики):
# Реалізуйте систему логіну/реєстрації для керування сайтом.
# Додайте можливість редагування існуючих сторінок.
# Створіть функціонал для пошуку сторінок за ключовими словами у заголовку або вмісті.
class Page:
    def __init__(self, title, content, publication_date):
        self.title = title
        self.content = content
        self.publication_date = publication_date

    def show_details(self):
        print(f"Page title: {self.title}. Page content: {self.content}. Page publication date: {self.publication_date}")

    def __str__(self):
        return f"Page title: {self.title}. Page content: {self.content}. Page publication date: {self.publication_date}"


class WebSite:
    def __init__(self, name, URL, owner_login, owner_password):
        self.name = name
        self.URL = URL
        self.owner_login = owner_login
        self.owner_password = owner_password
        self.pages = []

    def show_site_info(self):
        print(f"WebSite Name: {self.name}")
        print(f"WebSite URL: {self.URL}")

        if len(self.pages) == 0:
            print("This site has no pages")
            return

        print("Pages on the WebSite:")
        for page in self.pages:
            print(page)

    def add_page(self):
        page_title = input("Enter page title to add: ")
        page_content = input("Enter page content to add: ")
        page_publication_date = input("Enter publication date to add: ")

        for page in self.pages:
            if page.title == page_title:
                print("This page is already exists")
                return

        page = Page(page_title, page_content, page_publication_date)
        self.pages.append(page)
        print(f"Page with title {page_title} has been added")

    def edit_page(self):
        if len(self.pages) == 0:
            print("This site doesn't have pages")
            return


        current_page_title = input("Enter page title: ")
        new_page_title = input("Enter page title to edit: ")
        new_page_content = input("Enter page content to edit: ")
        new_page_publication_date = input("Enter publication date to edit: ")

        for page in self.pages:
            if page.title == current_page_title:
                page.title = new_page_title
                page.content = new_page_content
                page.publication_date = new_page_publication_date

                print("Page has been edited")
                return

        print(f"This page with title {current_page_title} doesn't exist")

    def search_page(self):
        if len(self.pages) == 0:
            print("This site doesn't have pages")
            return

        target_words = input("Enter text to search: ")

        for page in self.pages:
            if target_words in page.title or target_words in page.content:
                print(page)
                return

        print(f"Page with words \"{target_words}\" doesn't exist")

    def delete_page(self):
        if len(self.pages) == 0:
            print("This site doesn't have pages")
            return

        page_title = input("Enter page title to delete: ")

        for page in self.pages:
            if page.title == page_title:
                self.pages.remove(page)
                print("Page has been deleted")
                return

        print(f"This page with title {page_title} doesn't exist")


websites_database = []

def add_website():
    website_name = input("Enter WebSite Name: ")
    website_url = input("Enter WebSite URL: ")
    website_login= input("Enter WebSite Owner Login: ")
    website_password = input("Enter WebSite Owner Password: ")

    for website in websites_database:
        if website_name == website.name:
            print("This WebSite is already exists")
            return

    website = WebSite(website_name, website_url, website_login, website_password)
    websites_database.append(website)


def check_website():
    website_name = input("Enter WebSite Name: ")

    for website in websites_database:
        if website.name == website_name:
            return website

    return False


while True:
    user_choice = int(input("Select service: Create WebSite(1), Add Page to WebSite(2), Delete Page from WebSite(3). "
                            "Edit Page on WebSite(4). Show info about WebSite(5). Search Page on WebSite(6), Exit(7): "))

    if user_choice == 1:
        add_website()

    elif user_choice == 2:
        current_website = check_website()

        if not current_website:
            print("This WebSite doesn't exist")
            continue

        owner_check = input("Are you owner of this WebSite? y/n: ")

        if owner_check == "n":
            print("You cant edit this WebSite")
            continue

        login = input("Enter owner login: ")
        password = input("Enter owner password: ")

        if login != current_website.owner_login or password != current_website.owner_password:
            print("Wrong login or password")
            continue

        print("You are logged as WebSite owner")
        current_website.add_page()

    elif user_choice == 3:
        current_website = check_website()

        if not current_website:
            print("This WebSite doesn't exist")
            continue

        owner_check = input("Are you owner of this WebSite? y/n: ")

        if owner_check == "n":
            print("You cant edit this WebSite")
            continue

        login = input("Enter owner login: ")
        password = input("Enter owner password: ")

        if login != current_website.owner_login or password != current_website.owner_password:
            print("Wrong login or password")
            continue

        print("You are logged as WebSite owner")
        current_website.delete_page()

    elif user_choice == 4:
        current_website = check_website()

        if not current_website:
            print("This WebSite doesn't exist")
            continue

        owner_check = input("Are you owner of this WebSite? y/n: ")

        if owner_check == "n":
            print("You cant edit this WebSite")
            continue

        login = input("Enter owner login: ")
        password = input("Enter owner password: ")

        if login != current_website.owner_login or password != current_website.owner_password:
            print("Wrong login or password")
            continue

        print("You are logged as WebSite owner")
        current_website.edit_page()

    elif user_choice == 5:
        current_website = check_website()

        if current_website:
                current_website.show_site_info()

        else:
            print("This WebSite doesn't exist")

    elif user_choice == 6:
        current_website = check_website()

        if current_website:
                current_website.search_page()

        else:
            print("This WebSite doesn't exist")

    elif user_choice == 7:
        print("Exit from the program")
        break

    else:
        print("Enter a number 1-7")