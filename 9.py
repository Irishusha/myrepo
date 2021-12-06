from math import ceil
a=float(input())
b=float(input())
v=int(input())
if a < 0 or b < 0 :
    print("error")
else :
    V=round(((a*a*5)*b)/(v*1000))
    print(V)
    