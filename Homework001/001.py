# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# day = int(input("Введите число дня недели (от 0 до 9): "))
# if day == 1:
#     print("Понедельник")
# if day == 2:
#     print("Вторник")
# if day == 3:
#     print("Среда")
# if day == 4:
#     print("Четверг")
# if day == 5:
#     print("Пятница")
# if day == 6:
#     print("Суббота")
# if day == 7:
#     print("Воскресенье")
# if day == 0:
#     print("Такого дня не существует")
# if day == 8:
#     print("Такого дня не существует")
# if day == 9:
#     print("Такого дня не существует")
# else:
#     print("Спасибо! Ваш голос учтен!")




# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a
#
# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result
#
# statement = inputNumbers(3)
#
# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")





# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

# def inputCoordinates(x):
#     a = [0] * x
#     for i in range(x):
#         is_Ok = False
#         while not is_Ok:
#             try:
#                 number = float(input(f"Введите {i+1} координату: "))
#                 a[i] = number
#                 is_Ok = True
#                 if a[i] == 0:
#                     is_Ok = False
#                     print("Координата не должно быть равна 0 ")
#             except ValueError:
#                 print("Ты ошибся. Вводить надо числа!")
#     return a
#
# def checkCoordinates(xy):
#     text = 4
#     if xy[0] > 0 and xy[1] > 0:
#         text = 1
#     elif xy[0] < 0 and xy[1] > 0:
#         text = 2
#     elif xy[0] < 0 and xy[1] < 0:
#         text = 3
#     print(f"Точка находится в {text} четверти плоскости")
#
# Coordinate = inputCoordinates(2)
# checkCoordinates(Coordinate)


