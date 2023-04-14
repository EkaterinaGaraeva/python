# Задача 2: Найдите сумму цифр трехзначного числа.
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


def sum_of_digits_of_three_digit_number(num):
    if len(num) == 3:
        try:
            num = int(num)
            sum_of_digits = 0
            while num >= 1:
                sum_of_digits += num % 10
                num = int(num/10)
            print("Сумма цифр ->", sum_of_digits)
        except ValueError:
            print("Вы ввели не число")
    else:
        print("Вы ввели не трехзначное число")

n = input("Введите трехзначное число: ")
sum_of_digits_of_three_digit_number(n)

