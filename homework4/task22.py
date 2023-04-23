# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


def input_elements(count: int) -> list:
    list_of_numbers = []
    for i in range(count):
        num = int(input(f"Введите {i+1} число множества: "))
        list_of_numbers.append(num)
    return list_of_numbers

def common_elements_of_sets(list_one: list, list_two: list) -> list:
    set_one = set(list_one)
    set_two = set(list_two)
    result_set = set_one & set_two
    result_list = list(result_set)
    result_list.sort()
    return result_list

n = int(input("Введите количество элементов первого множества n: "))
m = int(input("Введите количество элементов второго множества m: "))
list1 = input_elements(n)
list2 = input_elements(m)
print(list1)
print(list2)
print(*common_elements_of_sets(list1, list2))

