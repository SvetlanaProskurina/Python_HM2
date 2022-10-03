# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11
def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


# input_ = input('Введите число \n')
# res = 0
# for i in input_:
#     if isint(i):
#         res+=int(i)
# print(res)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# res = 1
# lst = []
# input_ = input('Введите число \n')

# if isint(input_):
#     for i in range(1,int(input_)+1):
#         res*=i 
#         lst.append(res)
# print(lst)

# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

#     - Для n = 6: 14.07

# def power(base, exp):
#     if (exp == 1):
#         return (base)
#     if (exp != 1):
#         return (base * power(base, exp - 1))
# n = 0
# res = 0
# lst = []
# input_ = input('Введите число \n')

# if isint(input_):
#     for i in range(1,int(input_)+1):
#         n= power((1+1/i),i)
#         res+=n
# #        lst.append(str(round(n,3)))
# #print(lst) # для 6 : ['2.0', '2.25', '2.37', '2.441', '2.488', '2.522']
# print(str(round(res,3))[:-1])

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#    Найдите произведение элементов на указанных позициях. 
#    Позиции вводятся пользователем с клавиатуры. 5 2 8

#    [-5 -4 -3 -2 -1 0 1 2 3 4 5] -> -8

res = 1
lst = []

input_n = input('Введите число N \n')
if isint(input_n):
    for i in range(-int(input_n),int(input_n)+1):
        lst.append(i)
else:
    print ("надо было вводить числа")
    exit()
print(lst) 

input_index = input('Введите через пробел позиции элементов \n')
s = ".:;!_*+()/#%&"

for char in s:
    if char in input_index :
        print('введите верно, через пробел')
    else:
        in_index = input_index.split(" ")
# print(in_index)
if len(lst)>0:
    for i in in_index:
        if isint(i):
            if isint(lst[int(i)]):
                res*=lst[int(i)]
        else:
            print("надо было вводить числа")
            exit()
    # print(lst[int(i)])
    print(res)

# 5. Реализуйте алгоритм перемешивания списка.
# random.randint(2, 6)
# random.randrange(2, 6)
# '''
