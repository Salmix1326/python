# import requests
#
#
# response = requests.post("http://localhost:8000/hello")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)


# import requests
#
#
# response = requests.get("http://localhost:8000/greeting")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)
#
# response = requests.get("http://localhost:8001/greeting")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)

# import requests
#
#
# response = requests.post("http://localhost:8000/hello/Mary")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)
#
# name_data = {
#     "name": "John"
# }
#
# response = requests.post("http://localhost:8000/hello_json", json=name_data)
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)

import requests


while True:
    user_choice = input('Choose option\nTo get all books press (1)\nTo add new book press (2)').strip()

    if user_choice == '1':
        response = requests.get('http://localhost:8000/books')

        if response.ok:
            data = response.json()

            print(data)
        else:
            print(response.text)

    elif user_choice == '2':
        book_id = int(input('Please enter book\'s id: ').strip())
        book_title = input('Please enter book\'s title: ').strip()
        book_author = input('Please enter book\'s author: ').strip()
        book_year = int(input('Please enter book\'s year: ').strip())
        book_pages = int(input('Please enter book\'s pages quantity: ').strip())

        new_book = {
            "id": book_id,
            "title": book_title,
            "author": book_author,
            "year": book_year,
            "pages": book_pages
        }

        response = requests.post('http://localhost:8000/books', json=new_book)

        if response.ok:
            print('Book is added')
        else:
            print(response.text)

