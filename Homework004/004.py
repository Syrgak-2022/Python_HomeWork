# 1. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
#
# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)
#
# def rnd():
#     return random.randint(0, 101)
#
# def create_mn(k):
#     list = [rnd() for i in range(k + 1)]
#     return list
#
# def create_str(sp):
#     list = sp[::-1]
#     wr = ''
#     if len(list) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(list)):
#             if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
#                 wr += f'{list[i]}x^{len(list) - i - 1}'
#                 if list[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 2 and list[i] != 0:
#                 wr += f'{list[i]}x'
#                 if list[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 1 and list[i] != 0:
#                 wr += f'{list[i]} = 0'
#             elif i == len(list) - 1 and list[i] == 0:
#                 wr += ' = 0'
#     return wr
#
# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))










# 2. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


import random

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_mn(k):
    list = [rnd() for i in range(k + 1)]
    return list

def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list[i + 1] != 0 or list[i + 2] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] != 0 or list[i + 2] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    list = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        list.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l - 1
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            list.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            list.append(0)
            i += 1

    return lst


k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file34_1.txt", create_str(koef1))
write_file("file34_2.txt", create_str(koef2))

with open('file34_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file34_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
list1 = calc_mn(st1)
list2 = calc_mn(st2)
ll = len(list1)
if len(list1) > len(list2):
    ll = len(list2)
lst_new = [list1[i] + list2[i] for i in range(ll)]
if len(list1) > len(list2):
    mm = len(list1)
    for i in range(ll, mm):
        lst_new.append(list1[i])
else:
    mm = len(list2)
    for i in range(ll, mm):
        lst_new.append(list2[i])
write_file("file34_res.txt", create_str(lst_new))
with open('file34_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")