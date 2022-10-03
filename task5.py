# 5. Реализуйте алгоритм перемешивания списка.
# random.randint(2, 6)
# random.randrange(2, 6)
# '''
from random import randint


def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


lst = []

input_n = input('Введите число N \n')

if isint(input_n):
    for i in range(-int(input_n),int(input_n)+1):
        lst.append(i)
else:
    print ("надо было вводить числа")
    exit()
    
print(lst) 

lst_new = lst
length_lst_new = len(lst_new)-1

for i in range(length_lst_new):
    index_new = randint(0,length_lst_new)
    temp = lst_new[i]
    lst[i] = lst_new[index_new]
    lst_new[index_new] = temp
print(lst_new)