n=int(input())
z=n%1000
z3=z%10
z2=z%100//10
z1=z//100
#print(z3+z2+z1)
a=n//1000
a1=a%10
a2=a%100//10
a3=a//100
#print(a1+a2+a3)
if a1+a2+a3 == z1+z2+z3:
    print("Счастливый")
else :
    print("Обычный")

