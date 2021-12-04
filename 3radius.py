from math import sqrt, sin

x_a=float(input())

y_a=float(input())

x_b=float(input())

y_b=float(input())

x_c=float(input())

y_c=float(input())

c = sqrt(((x_b-x_a)**2+(y_b-y_a)**2))
a = sqrt(((x_c-x_b)**2+(y_c-y_b)**2))
b = sqrt(((x_c-x_a)**2+(y_c-y_a)**2))
ab=a+b
ac=a+c
cb=c+b
if ab>c and ac>b and cb>a :
    p=a+b+c
    rad=round(sqrt((p/2 - a)*(p/2 - b)*(p/2 - c)/(p/2)),4)
  #  r =       sqrt((p/2 - a)*(p/2 - b)*(p/2 - c)/(p/2))
    s=sqrt((p/2)*((p/2)-a)*((p/2)-b)*((p/2)-c))
    radius_opis=round((a*b*c)/(4*s),4)
    m_a=0.5*sqrt(2*(c**2+b**2)-a**2)
    m_b=0.5*sqrt(2*(a**2+c**2)-b**2)
    m_c=0.5*sqrt(2*(a**2+b**2)-c**2)
    m=round(m_a+m_b+m_c,4)
    print(rad, radius_opis, m)
else:
   print("error")