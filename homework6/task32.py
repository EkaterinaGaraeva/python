# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


def search_for_indexes(list_of_nums, min_element, max_element):
    list_of_indexes = [i for i in range(len(list_of_numbers)) if min_element <= list_of_numbers[i] <= max_element]
    return list_of_indexes

list_of_numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input("Введите минимум: "))
max_number = int(input("Введите максимум: "))
indexes = search_for_indexes(list_of_numbers, min_number, max_number)
print(indexes)

