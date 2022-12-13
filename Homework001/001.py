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

