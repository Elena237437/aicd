#!/usr/bin/env python
# coding: utf-8

# Политова Елена ИД23-3 (3 вар по сп.)

# (35) Создайте двусвязный список для хранения информации о задачах в проекте. Каждый элемент списка должен содержать название задачи, описание, дату начала и дату окончания.

# In[3]:


class Task:
    # Конструктор класса Task для инициализации задачи с необходимыми атрибутами
    def __init__(self, name, description, start_date, end_date):
        self.name = name  # Название задачи
        self.description = description  # Описание задачи
        self.start_date = start_date  # Дата начала задачи
        self.end_date = end_date  # Дата окончания задачи
        self.prev = None  # Ссылка на предыдущую задачу в списке
        self.next = None  # Ссылка на следующую задачу в списке

class DoublyLinkedList:
    # Конструктор класса DoublyLinkedList для инициализации пустого списка
    def __init__(self):
        self.head = None  # Указатель на начало списка
        self.tail = None  # Указатель на конец списка

    # Метод для добавления новой задачи в конец списка
    def append(self, name, description, start_date, end_date):
        new_task = Task(name, description, start_date, end_date)  # Создание новой задачи
        if self.head is None:  # Если список пуст
            self.head = self.tail = new_task  # Новая задача становится и началом и концом списка
        else:
            self.tail.next = new_task  # Ссылка на следующую задачу у текущего конца списка указывает на новую задачу
            new_task.prev = self.tail  # Ссылка на предыдущую задачу у новой задачи указывает на текущий конец списка
            self.tail = new_task  # Новая задача становится концом списка

    # Метод для удаления задачи по названию
    def remove(self, name):
        current = self.head  # Начало поиска с головы списка
        while current:  # Пока текущий элемент не равен None
            if current.name == name:  # Если название текущей задачи совпадает с искомым
                if current.prev:  # Если текущая задача не является первой
                    current.prev.next = current.next  # Перепривязка ссылки у предыдущей задачи
                if current.next:  # Если текущая задача не является последней
                    current.next.prev = current.prev  # Перепривязка ссылки у следующей задачи
                if current == self.head:  # Если текущая задача является первой
                    self.head = current.next  # Голова списка теперь указывает на следующую задачу
                if current == self.tail:  # Если текущая задача является последней
                    self.tail = current.prev  # Хвост списка теперь указывает на предыдущую задачу
                return  # Завершение работы метода после удаления задачи
            current = current.next  # Переход к следующей задаче

    # Метод для вывода всех задач в списке
    def display(self):
        current = self.head  # Начало вывода с головы списка
        while current:  # Пока текущий элемент не равен None
            print(f"Name: {current.name}, Description: {current.description}, Start: {current.start_date}, End: {current.end_date}")
            current = current.next  # Переход к следующей задаче

# Пример использования
tasks = DoublyLinkedList()  # Создание пустого двусвязного списка задач
tasks.append("Task 1", "Description 1", "2024-05-01", "2024-05-05")  # Добавление задачи
tasks.append("Task 2", "Description 2", "2024-05-06", "2024-05-10")  # Добавление задачи
tasks.append("Task 3", "Description 3", "2024-05-11", "2024-05-15")  # Добавление задачи

tasks.display()  # Вывод всех задач

tasks.remove("Task 2")  # Удаление задачи по названию

tasks.display()  # Вывод всех задач после удаления


# (36)Реализовать функцию, которая проверяет, является ли двусвязный список палиндромом.

# In[4]:


class Node:
    def __init__(self, data):
        # Инициализация узла
        self.data = data
        self.next = None  # Указатель на следующий узел
        self.prev = None  # Указатель на предыдущий узел

class DoublyLinkedList:
    def __init__(self):
        # Инициализация пустого двусвязного списка
        self.head = None
        self.tail = None

    def append(self, data):
        # Добавление нового узла в конец списка
        new_node = Node(data)
        if self.head is None:
            # Если список пуст, новый узел становится головой и хвостом
            self.head = new_node
            self.tail = new_node
        else:
            # Иначе, добавляем новый узел в конец списка
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

def is_palindrome(dll):
    # Функция для проверки, является ли двусвязный список палиндромом
    if dll.head is None:
        # Пустой список считается палиндромом
        return True
    
    # Инициализация указателей на начало и конец списка
    left = dll.head
    right = dll.tail
    
    # Проверка элементов с обеих сторон
    while left != right and left.prev != right:
        if left.data != right.data:
            # Если элементы не равны, список не является палиндромом
            return False
        # Смещение указателей к центру
        left = left.next
        right = right.prev
    
    # Если все элементы проверены и равны, список является палиндромом
    return True

# Пример использования
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(1)

print(is_palindrome(dll))  # Вывод: True


# class Node: - Определение класса для узла двусвязного списка.
# def __init__(self, data): - Инициализация узла с данными, указателями на следующий и предыдущий узлы.
# self.data = data - Сохранение данных узла.
# self.next = None - Инициализация указателя на следующий узел.
# self.prev = None - Инициализация указателя на предыдущий узел.
# class DoublyLinkedList: - Определение класса для двусвязного списка.
# def __init__(self): - Инициализация пустого списка.
# self.head = None - Инициализация указателя на голову списка.
# self.tail = None - Инициализация указателя на хвост списка.
# def append(self, data): - Метод для добавления нового узла в конец списка.
# new_node = Node(data) - Создание нового узла с заданными данными.
# if self.head is None: - Проверка, пуст ли список.
# self.head = new_node - Новый узел становится головой списка.
# self.tail = new_node - Новый узел становится хвостом списка.
# self.tail.next = new_node - Связывание текущего хвоста с новым узлом.
# new_node.prev = self.tail - Связывание нового узла с текущим хвостом.
# self.tail = new_node - Обновление указателя на хвост списка.
# def is_palindrome(dll): - Определение функции для проверки, является ли список палиндромом.
# if dll.head is None: - Проверка, пуст ли список.
# return True - Пустой список считается палиндромом.
# left = dll.head - Инициализация указателя на начало списка.
# right = dll.tail - Инициализация указателя на конец списка.
# while left != right and left.prev != right: - Проверка, пока указатели не встретятся.
# if left.data != right.data: - Сравнение данных в узлах.
# return False - Если данные не равны, список не является палиндромом.
# left = left.next - Смещение указателя на следующий узел.
# right = right.prev - Смещение указателя на предыдущий узел.
# return True - Если все элементы равны, список является палиндромом.
# dll = DoublyLinkedList() - Создание нового двусвязного списка.
# dll.append(1) и далее - Добавление элементов в список.
# print(is_palindrome(dll)) - Проверка и вывод результата.

# (37)Реализовать функцию, которая переворачивает циклический двусвязный список.

# In[5]:


class Node:
    def __init__(self, data):
        self.data = data  # Содержимое узла
        self.next = None  # Ссылка на следующий узел
        self.prev = None  # Ссылка на предыдущий узел

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None  # Изначально список пуст, поэтому голова = None

    def append(self, data):
        new_node = Node(data)  # Создаем новый узел
        if not self.head:
            # Если список пуст, инициализируем голову
            self.head = new_node
            new_node.next = new_node  # Указываем, что следующий узел — это сам узел
            new_node.prev = new_node  # Указываем, что предыдущий узел — это сам узел
        else:
            # Если список не пуст
            tail = self.head.prev  # Последний узел в списке
            tail.next = new_node  # Последний узел указывает на новый узел как на следующий
            new_node.prev = tail  # Новый узел указывает на предыдущий узел (бывший хвост)
            new_node.next = self.head  # Новый узел указывает на голову как на следующий
            self.head.prev = new_node  # Головной узел указывает на новый узел как на предыдущий

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()

    def reverse(self):
        if not self.head:
            return  # Если список пуст, ничего не делаем

        current = self.head  # Начинаем с головы списка
        prev_node = None  # Переменная для хранения предыдущего узла
        while True:
            next_node = current.next  # Сохраняем следующий узел
            current.next = prev_node  # Меняем направление: текущий узел указывает на предыдущий
            current.prev = next_node  # Предыдущий узел текущего узла теперь становится следующим
            prev_node = current  # Сдвигаем предыдущий узел на текущий
            current = next_node  # Сдвигаем текущий узел на следующий
            if current == self.head:
                break  # Если дошли до головы, заканчиваем цикл

        self.head.next = prev_node  # Голова теперь указывает на предыдущий узел
        self.head.prev = current  # Головной узел теперь указывает на текущий узел как на предыдущий
        self.head = prev_node  # Перемещаем голову на последний узел (который стал первым)

# Пример использования
dll = DoublyCircularLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Original list:")
dll.display()

dll.reverse()

print("Reversed list:")
dll.display()


# (38)Необходимо отсортировать массив строк по алфавиту и вывести результат на экран. Использовать алгоритмы сортировки: сортировку пузырьком, сортировку слиянием и быструю сортировку. Сравнить время выполнения алгоритмов сортировки с помощью декоратора. Строки хранятся в файле.

# In[6]:


import time
import functools

# Декоратор для измерения времени выполнения функции
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # Начальное время
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # Конечное время
        run_time = end_time - start_time    # Общее время выполнения
        print(f"Функция {func.__name__!r} выполнена за {run_time:.4f} секунд")
        return value
    return wrapper_timer

# Считываем строки из файла
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Пузырьковая сортировка
@timer
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Сортировка слиянием
@timer
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Быстрая сортировка
@timer
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Основная часть программы
if __name__ == "__main__":
    filename = 'strings.txt'  # Имя файла с массивом строк

    # Считывание строк из файла
    strings = read_file(filename)
    print("Исходный массив строк:")
    print(strings)

    # Копирование массивов для сортировки
    bubble_sorted_strings = strings[:]
    merge_sorted_strings = strings[:]
    quick_sorted_strings = strings[:]

    # Сортировка и вывод результатов
    print("\nПузырьковая сортировка:")
    bubble_sorted_strings = bubble_sort(bubble_sorted_strings)
    print(bubble_sorted_strings)

    print("\nСортировка слиянием:")
    merge_sorted_strings = merge_sort(merge_sorted_strings)
    print(merge_sorted_strings)

    print("\nБыстрая сортировка:")
    quick_sorted_strings = quick_sort(quick_sorted_strings)
    print(quick_sorted_strings)


# (39)Реализовать класс бинарного дерева. Написать функцию для поиска наименьшего и наибольшего элементов в бинарном дереве.

# In[ ]:


class TreeNode:
    def __init__(self, key):
        # Конструктор узла бинарного дерева
        self.left = None    # Левый потомок
        self.right = None   # Правый потомок
        self.val = key      # Значение узла

class BinaryTree:
    def __init__(self):
        # Конструктор бинарного дерева
        self.root = None    # Корень дерева

    def insert(self, key):
        # Вставка нового узла с заданным значением
        if self.root is None:
            # Если корень пуст, новый узел становится корнем
            self.root = TreeNode(key)
        else:
            # Иначе, вставляем рекурсивно
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        # Рекурсивная функция для вставки нового узла
        if key < node.val:
            # Если значение меньше текущего узла, идем влево
            if node.left is None:
                # Если левый потомок пуст, создаем новый узел здесь
                node.left = TreeNode(key)
            else:
                # Иначе продолжаем рекурсивно вставлять в левое поддерево
                self._insert_recursive(node.left, key)
        else:
            # Если значение больше или равно текущему узлу, идем вправо
            if node.right is None:
                # Если правый потомок пуст, создаем новый узел здесь
                node.right = TreeNode(key)
            else:
                # Иначе продолжаем рекурсивно вставлять в правое поддерево
                self._insert_recursive(node.right, key)

    def find_min(self):
        # Поиск наименьшего значения в дереве
        current = self.root
        # Идем по левым потомкам до самого нижнего узла
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self):
        # Поиск наибольшего значения в дереве
        current = self.root
        # Идем по правым потомкам до самого нижнего узла
        while current.right is not None:
            current = current.right
        return current.val


# (40)Даны две двоичные кучи. Напишите функцию, которая объединяет эти две кучи в одну.

# In[ ]:


import heapq

def merge_heaps(heap1, heap2):
    # Объединяем два списка, которые представляют собой кучи, в один с помощью heapq.merge
    merged = list(heapq.merge(heap1, heap2))
    
    # Превращаем полученный список в кучу с помощью heapq.heapify
    heapq.heapify(merged)
    
    return merged

# Пример использования функции
heap1 = [1, 3, 5, 7]
heap2 = [2, 4, 6, 8]

result = merge_heaps(heap1, heap2)
print(result)


# (41)а) Создать класс «Клиент» с полями «Имя», «Фамилия», «Адрес» и «Номер телефона». Создать хеш-таблицу для хранения объектов класса «Клиент» по ключу — номеру клиентской карты.
# б) Написать функцию для удаления всех элементов из хеш-таблицы, которые не удовлетворяют заданному условию.
# в) Реализуйте хеш-таблицу для хранения информации о студентах университета. Ключом является номер студенческого билета, значение — объект, содержащий информацию о студенте (ФИО, группа, оценки и т.д.). Используйте метод разрешения коллизий методом цепочек.

# In[ ]:


# a) Создать класс «Клиент» с полями «Имя», «Фамилия», «Адрес» и «Номер телефона»
class Client:
    def __init__(self, first_name, last_name, address, phone_number):
        self.first_name = first_name  # Имя
        self.last_name = last_name  # Фамилия
        self.address = address  # Адрес
        self.phone_number = phone_number  # Номер телефона

    def __repr__(self):
        return f"Client({self.first_name}, {self.last_name}, {self.address}, {self.phone_number})"

# Создать хеш-таблицу для хранения объектов класса «Клиент» по ключу — номеру клиентской карты
class ClientHashTable:
    def __init__(self):
        self.table = {}  # Инициализация пустой хеш-таблицы

    def add_client(self, card_number, client):
        self.table[card_number] = client  # Добавление клиента в таблицу по номеру карты

    def remove_clients(self, condition):
        # Удаление клиентов, которые не удовлетворяют заданному условию
        keys_to_remove = [key for key, client in self.table.items() if not condition(client)]
        for key in keys_to_remove:
            del self.table[key]

    def __repr__(self):
        return f"ClientHashTable({self.table})"

# Пример использования
client_table = ClientHashTable()
client_table.add_client(123, Client("Иван", "Иванов", "ул. Ленина, 1", "555-1234"))
client_table.add_client(456, Client("Мария", "Смирнова", "ул. Пушкина, 2", "555-5678"))

# Условие: оставлять только клиентов с фамилией "Иванов"
condition = lambda client: client.last_name == "Иванов"
client_table.remove_clients(condition)

print(client_table)

# б) Реализовать хеш-таблицу для хранения информации о студентах университета
class Student:
    def __init__(self, full_name, group, grades):
        self.full_name = full_name  # Полное имя студента
        self.group = group  # Группа студента
        self.grades = grades  # Оценки студента

    def __repr__(self):
        return f"Student({self.full_name}, {self.group}, {self.grades})"

class StudentHashTable:
    def __init__(self, size=10):
        self.size = size  # Размер таблицы
        self.table = [[] for _ in range(size)]  # Инициализация таблицы списков для метода цепочек

    def _hash_function(self, student_id):
        return student_id % self.size  # Хеш-функция для получения индекса

    def add_student(self, student_id, student):
        index = self._hash_function(student_id)  # Получение индекса по хеш-функции
        self.table[index].append((student_id, student))  # Добавление студента в список по индексу

    def get_student(self, student_id):
        index = self._hash_function(student_id)  # Получение индекса по хеш-функции
        for id, student in self.table[index]:
            if id == student_id:
                return student  # Возврат студента по ID
        return None  # Студент не найден

    def __repr__(self):
        return f"StudentHashTable({self.table})"

# Пример использования
student_table = StudentHashTable()
student_table.add_student(1001, Student("Алексей Иванов", "ИС101", [90, 85, 92]))
student_table.add_student(1002, Student("Ольга Петрова", "ИС102", [78, 82, 88]))
student_table.add_student(1011, Student("Дмитрий Смирнов", "ИС101", [95, 91, 89]))

print(student_table)
print(student_table.get_student(1001))
print(student_table.get_student(1011))

# в) Реализовать хеш-таблицу для хранения информации о студентах университета с разрешением коллизий методом цепочек
class UniversityStudent:
    def __init__(self, full_name, group, grades):
        self.full_name = full_name  # Полное имя студента
        self.group = group  # Группа студента
        self.grades = grades  # Оценки студента

    def __repr__(self):
        return f"UniversityStudent({self.full_name}, {self.group}, {self.grades})"

class UniversityStudentHashTable:
    def __init__(self, size=10):
        self.size = size  # Размер таблицы
        self.table = [[] for _ in range(size)]  # Инициализация таблицы списков для метода цепочек

    def _hash_function(self, student_id):
        return student_id % self.size  # Хеш-функция для получения индекса

    def add_student(self, student_id, student):
        index = self._hash_function(student_id)  # Получение индекса по хеш-функции
        self.table[index].append((student_id, student))  # Добавление студента в список по индексу

    def get_student(self, student_id):
        index = self._hash_function(student_id)  # Получение индекса по хеш-функции
        for id, student in self.table[index]:
            if id == student_id:
                return student  # Возврат студента по ID
        return None  # Студент не найден

    def __repr__(self):
        return f"UniversityStudentHashTable({self.table})"

# Пример использования
university_student_table = UniversityStudentHashTable()
university_student_table.add_student(1001, UniversityStudent("Алексей Иванов", "ИС101", [90, 85, 92]))
university_student_table.add_student(1002, UniversityStudent("Ольга Петрова", "ИС102", [78, 82, 88]))
university_student_table.add_student(1011, UniversityStudent("Дмитрий Смирнов", "ИС101", [95, 91, 89]))

print(university_student_table)
print(university_student_table.get_student(1001))
print(university_student_table.get_student(1011))

