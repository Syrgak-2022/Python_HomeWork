# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def inputNums(inputText):
#     is_Ok = False
#     while not is_Ok:
#         try:
#             number = float(input(f"{inputText}"))
#             is_Ok = True
#         except ValueError:
#             print("Это не число!")
#     return number
#
# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum
#
# num = inputNums("Введите число: ")
#
# print(f"Сумма цифр = {sumNums(num)}")





# 2. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

# n = int(input("Введите количество чисел в последовательности: "))
#
# numbers = []
#
# for i in range(0, n):
#     input_value = int(input(f"Введите число №{i+1}: "))
#     numbers.append(input_value)
#
# sum = 0
# for i in numbers:
#     sum += i
#
# print("Сумма всех чисел последовательности:", sum)





# 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# from time import time
# lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# def mix_list(old: list) -> list:
#     new = []
#     while old:
#         x = str(time()).split('.')[1]
#         x = list(map(int, [x[0], x[-1]]))
#         x = x[0] if x[0] <= x[1] else x[1]
#         if x > len(old)-1:
#             new.append(old.pop(0))
#         else:
#             new.append(old.pop(x))
#     return new
#
# lister = mix_list(lister)
# print(lister)