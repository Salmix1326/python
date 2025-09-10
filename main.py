# Завдання 1
#==================================================================================================
# Створіть клас однозв’язного списку SinglyLinkedList
# Методи
# print() – виводить список на екран
# push_end(data) – добавити в кінець
# push_start(data) – добавити на початку
# pop_start() – видалити перший елемент

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def print(self):
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.value, end=" -> ")
            temp_node = temp_node.next

        print()

    def push_end(self, data): # 0(1)
        if not self.is_empty():
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node

        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def push_start(self, data): # 0(1)
        if not self.is_empty():
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def pop_start(self):
        if self.head != self.tail:
            temp_node = self.head
            self.head = self.head.next
            temp_node.next = None
        else:
            self.head = None
            self.tail = None

    def get_item(self, pos):
        counter = 0
        temp_node = self.head

        while counter != pos - 1:
            counter += 1
            temp_node = temp_node.next

        return temp_node.value


new_list = SinglyLinkedList()
new_list.push_end(5)
new_list.push_end(10)
new_list.push_end(15)
new_list.push_start(25)
res = new_list.get_item(4)
print(res)
new_list.print()