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