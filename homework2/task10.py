# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2


import random

def min_count_of_coins(num, coins):
    sum_of_coins = sum(coins)
    count = 0
    if sum_of_coins <= (num - sum_of_coins):
        count = sum_of_coins
    else:
        count = num - sum_of_coins
    return count

n = int(input("Введите количество монеток: "))
list_of_coins = [random.randint(0, 1) for i in range(0, n)]
print(list_of_coins)
print(f"Минимальное количество монет, которые нужно перевернуть = {min_count_of_coins(n, list_of_coins)}")

