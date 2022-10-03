# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


res = 1
lst = []
input_ = input('Введите число \n')

if isint(input_):
    for i in range(1,int(input_)+1):
        res*=i 
        lst.append(res)
print(lst)