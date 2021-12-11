# вычисляется площадь треугольника по формуле Герона
from math import sqrt
a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
#else :
#    print("ошибка")