# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


import random

def dictionary_of_difference(list_of_numbers, number):
    dict_of_diff = {}
    for i in list_of_numbers:
        if i >= number:
            diff_key = i - number
            if diff_key not in dict_of_diff.keys():
                dict_of_diff[diff_key] = {i}
            else:
                dict_of_diff[diff_key].add(i)
        else:
            diff_key = number - i
            if diff_key not in dict_of_diff.keys():
                dict_of_diff[diff_key] = {i}
            else:
                dict_of_diff[diff_key].add(i)
    return dict_of_diff

def close_number(dictionary):
    min_key = min(dictionary.keys())
    close_num = dictionary[min_key]
    return close_num

n = int(input("Введите количество элементов в массиве N: "))
list_1 = [random.randint(0, 9) for i in range(0, n)]
print(list_1)
x = int(input("Введите число X: "))
dict_1 = dictionary_of_difference(list_1, x)
print(dict_1)
print(f"Самый(ые) близкий(ие) к Х = {x} элемент(ы) - ", end="")
close_num = close_number(dict_1)
if len(close_num) == 1:
    print(*close_num)
else:
    close_num1, close_num2 = close_num
    print(f"{close_num1} и {close_num2}")

