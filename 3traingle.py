from math import sqrt, cos,pi
x_a=float(input())
y_a=float(input())
x_b=float(input())
y_b=float(input())
x_c=float(input())
y_c=float(input())
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
    r=sqrt(((p/2-a)*(p/2-b)*(p/2-c))/(p/2))
    print("Радиус вписанной окружности в треугольник: ", r)
    s=sqrt(p/2*(p/2-a)*(p/2-b)*(p/2-c))
    print("Площадь треугольника: ", s)
    radius_opis=(a*b*c)/(4*s)
    print("Радиус описанной окружности: ", radius_opis)
    m_a=0.5*sqrt(2*(c**2+b**2)-a**2)
    m_b=0.5*sqrt(2*(a**2+c**2)-b**2)
    m_c=0.5*sqrt(2*(a**2+b**2)-c**2)
    m=round(m_a+m_b+m_c,4)
    print("Сумма длин медиан: ", m)
    print(r, radius_opis, m)
else:
    print("error")