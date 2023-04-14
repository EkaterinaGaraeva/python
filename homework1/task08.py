# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
#
# 3 2 4 -> yes
# 3 2 1 -> no

def chocolate(size_one, size_two, count):
    if (count <= size_one * size_two and count % size_one == 0) or (count <= size_one * size_two and count % size_two == 0):
        print("Можно")
    else:
        print("Нельзя")

print("Введите размеры шоколадки:")
n = int(input(f"n = "))
m = int(input(f"m = "))
k = int(input(f"Количество долек, которые нужно отломить k = "))
chocolate(n, m, k)

