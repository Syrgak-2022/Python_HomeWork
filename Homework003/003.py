# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_odd_index(list):
#     s = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             s += list[i]
#     print(f"Сумма равна: {s}")
#
# list = [2, 3, 5, 9, 3]
# sum_odd_index(list)
# list = list(map(int, input("Введите числа через пробел:\n").split()))
# sum_odd_index(list)





# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


# def multi_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)
#
# lst = [2, 3, 4, 5, 6]
# multi_lst(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# multi_lst(lst)