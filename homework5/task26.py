# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def degree_of_number(num_a: int, num_b: int) -> int:
    if num_b == 1:
        return num_a
    return num_a * degree_of_number(num_a, num_b - 1)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(f"{a} ** {b} = {degree_of_number(a, b)}")
print(f"Проверка: {a} ** {b} = {a**b}")

