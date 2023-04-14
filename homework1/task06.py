# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
#
# 385916 -> yes
# 123456 -> no


def sum_of_numbers(number):
    sum_of_digits = 0
    while number >= 1:
        sum_of_digits += number % 10
        number = int(number / 10)
    return sum_of_digits

def lucky_ticket(num):
    if num.isdigit() and len(num) == 6:
        num = int(num)
        n1 = num // 1000
        n2 = num % 1000
        sum1 = sum_of_numbers(n1)
        sum2 = sum_of_numbers(n2)
        print(f"{n1} -> {sum1}")
        print(f"{n2} -> {sum2}")
        if sum1 == sum2:
            print("Счастливый билет")
        else:
            print("Нет")
    else:
        print("Неверный формат номера билета")

n = input("Введите номер билета: ")
lucky_ticket(n)


