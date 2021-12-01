# Геометрическая задачка, расчет длин сторон, площадь, перимент треуголиника и величину его углов
from math import degrees, sin, sqrt,acos
x_a= float(input("Введите координату х т.А:"))
y_a= float(input("Введите координату у т.А:"))
x_b= float(input("Введите координату х т.В:"))
y_b= float(input("Введите координату у т.В:"))
x_c= float(input("Введите координату х т.С:"))
y_c= float(input("Введите координату у т.С:"))
c = sqrt(((x_b-x_a)**2+(y_b-y_a)**2))
print(c)
a = sqrt(((x_c-x_b)**2+(y_c-y_b)**2))
print(c)
b = sqrt(((x_c-x_a)**2+(y_c-y_a)**2))
print(b)
ab=a+b
ac=a+c
cb=c+b
if ab>c or ac>b or cb>a :
    print("Треугольник существует!")
    p=a+b+c
    print("Периметр треугольника:",p)
    s=sqrt(p/2*(p/2-a)*(p/2-b)*(p/2-c))
    print("Площадь треугольника: ", s)
    angle_A=degrees(acos((c**2+b**2-a**2)/(2*c*b)))
    angle_B=degrees(acos((c**2+a**2-b**2)/(2*c*a)))
    angle_C=degrees(acos((a**2+b**2-c**2)/(2*a*b)))
    print ("Угол А:",angle_A)
    print ("Угол B:",angle_B)
    print ("Угол C:",angle_C)
else :
    print("Не верные координаты, треугольник построить не возможно!")