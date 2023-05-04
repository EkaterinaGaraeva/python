# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


def filling_in_progression(first_element, diff, count):
    list_of_progression_elem = [(first_element + i * diff) for i in range(count)]
    return list_of_progression_elem

first_element_of_progression = int(input("Введите первый элемент арифметической прогрессии: "))
difference = int(input("Введите разность между элементами: "))
count_of_elements = int(input("Введите количество элементов прогрессии: "))

list_of_progression_elements = filling_in_progression(first_element_of_progression, difference, count_of_elements)
print(*list_of_progression_elements)

