# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9


import random

def maximum_number_of_berries(list_one: list) -> int:
    max_sum_of_berries = 0
    for i in range(len(list_one)):
        if i == 0:
            sum_of_berries = list_one[-1] + list_one[i] + list_one[i + 1]
        elif i == len(list_one) - 1:
            sum_of_berries = list_one[i - 1] + list_one[i] + list_one[0]
        else:
            sum_of_berries = list_one[i - 1] + list_one[i] + list_one[i + 1]
        if sum_of_berries > max_sum_of_berries:
            max_sum_of_berries = sum_of_berries
    return max_sum_of_berries

n = int(input("Введите количество кустов: "))
yield_list = [random.randint(1, 5) for i in range(n)]
print(*yield_list)
print(maximum_number_of_berries(yield_list))

