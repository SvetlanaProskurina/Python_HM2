# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

#     - Для n = 6: 14.07
def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))

        
n = 0
res = 0
lst = []
input_ = input('Введите число \n')

if isint(input_):
    for i in range(1,int(input_)+1):
        n= power((1+1/i),i)
        res+=n
#        lst.append(str(round(n,3)))
#print(lst) # для 6 : ['2.0', '2.25', '2.37', '2.441', '2.488', '2.522']
print(str(round(res,3))[:-1])
