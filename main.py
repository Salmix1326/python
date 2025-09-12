class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if not self.tail:
            return None

        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def pop_start(self):
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.head:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data


# Завдання 1
#=============================================================================================================
# Використовуючи класи з практичної реалізуйте клас Shop з трьома чергами до кас.
# Кожна черга реалізується через двозв’язний список
# Атрибути:
# queue1, queue2, queue3 – черги до кас
# Методи
# add_buyer(name, idx) – додає покупця в кінець черги номер idx
# serve_buyer(idx) – обслуговує покупця з черги idx(вивести повідомлення та видалити покупця з черги)
# Якщо черга стала порожньою, то викликати reorder(idx)
# reorder(idx) – з усіх черг останній покупець переходить в чергу з номером idx
# display_info() – виводить на екран 3 черги

class Shop:
    def __init__(self, queue1,queue2, queue3):
        self.queue1 = queue1
        self.queue2 = queue2
        self.queue3 = queue3

    def add_buyer(self, name, idx):
        if idx == 1:
            self.queue1.push_end(name)

        elif idx == 2:
            self.queue2.push_end(name)

        elif idx == 3:
            self.queue3.push_end(name)

    def serve_buyer(self, idx):
        if idx == 1:
            if self.queue1.head is not None:
                print(f"Buyer {self.queue1.head.data} is served and delete from the system")
                self.queue1.pop_start()

            if self.queue1.head is None:
                self.reorder(1)

        elif idx == 2:
            if self.queue2.head is not None:
                print(f"Buyer {self.queue2.head.data} is served and delete from the system")
                self.queue2.pop_start()

            if self.queue2.head is None:
                self.reorder(2)

        elif idx == 3:
            if self.queue3.head is not None:
                print(f"Buyer {self.queue3.head.data} is served and delete from the system")
                self.queue3.pop_start()

            if self.queue3.head is None:
                self.reorder(3)

    def reorder(self, idx):
        if idx == 1:
            if self.queue2.tail is not None:
                self.queue1.push_end(self.queue2.tail.data)
                self.queue2.pop_end()

            if self.queue3.tail is not None:
                self.queue1.push_end(self.queue3.tail.data)
                self.queue3.pop_end()

        elif idx == 2:
            if self.queue1.tail is not None:
                self.queue2.push_end(self.queue1.tail.data)
                self.queue1.pop_end()

            if self.queue3.tail is not None:
                self.queue2.push_end(self.queue3.tail.data)
                self.queue3.pop_end()

        elif idx == 3:
            if self.queue1.tail is not None:
                self.queue3.push_end(self.queue1.tail.data)
                self.queue1.pop_end()

            if self.queue2.tail is not None:
                self.queue3.push_end(self.queue2.tail.data)
                self.queue2.pop_end()

    def display_info(self):
            print(self.queue1)
            print(self.queue2)
            print(self.queue3)


queue1 = DoubleLinkedList()
queue2 = DoubleLinkedList()
queue3 = DoubleLinkedList()

shop = Shop(queue1, queue2, queue3)

shop.add_buyer("Олег", 1)
shop.add_buyer("Марина", 2)
shop.add_buyer("Марія", 2)
shop.add_buyer("Андрій", 3)
shop.add_buyer("Ірина", 1)
shop.add_buyer("Василь", 2)
shop.add_buyer("Тетяна", 3)
shop.add_buyer("Сергій", 3)
shop.add_buyer("Анна", 3)

print("Черги:")
shop. display_info()

shop.serve_buyer(1)
shop.serve_buyer(2)
shop.serve_buyer(3)

print("Після обслуговування покупців:")
shop. display_info()
shop.serve_buyer(1)

print("Покупці перейшли до вільної каси:")
shop. display_info()
