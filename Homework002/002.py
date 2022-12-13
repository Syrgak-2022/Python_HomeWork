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