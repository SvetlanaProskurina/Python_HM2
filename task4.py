# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#    Найдите произведение элементов на указанных позициях. 
#    Позиции вводятся пользователем с клавиатуры. 5 2 8

#    [-5 -4 -3 -2 -1 0 1 2 3 4 5] -> -8
def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

        
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