# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1


import random

def count_of_numbers(list_of_numbers, number):
    count = 0
    for i in list_of_numbers:
        if i == number:
            count += 1
    return count

n = int(input("Введите количество элементов в массиве N: "))
list_1 = [random.randint(0, 9) for i in range(0, n)]
print(list_1)
x = int(input("Введите число X: "))
print(f"Число X = {x} встречатся {count_of_numbers(list_1, x)} раз(а)")

