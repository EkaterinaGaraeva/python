# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3


import math

def guessed_numbers(sum_of_num, prod_of_num):
    # s = x + y
    # p = x * y
    # y = s - x
    # p = x * (s - x)
    # x^2 - s*x + p = 0
    # a = 1
    # b = -sum_of_num
    # c = prod_of_num
    # D = b**2 - 4*a*c
    D = sum_of_num**2 - 4 * prod_of_num
    # print(D)
    if D > 0:
        # x1 = (sum_of_num + math.sqrt(D))/2
        # x2 = (sum_of_num - math.sqrt(D))/2
        x = (sum_of_num + math.sqrt(D))/2
        # y1 = sum_of_num - x1
        # y2 = sum_of_num - x2
        y = sum_of_num - x
    elif D == 0:
        # x = - b / (2*a)
        x = sum_of_num / 2
        # y = sum_of_num - x
        y = x
    else:
        x = None
        y = None
    return (x, y)

s = int(input("Введите сумму чисел S = "))
p = int(input("Введите произведение чисел P = "))

x, y = guessed_numbers(s, p)
if x != None and y != None:
    print(f"X = {round(x, 3)}, Y = {round(y, 3)}")
else:
    print("Решения нет")

