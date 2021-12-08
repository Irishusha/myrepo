#расчитывает значение угла в градусах между стрелкой часов 12:00 и введенными данными
h=int(input())
m=int(input())
s=int(input())
if h<0 or h>=12 or m<0 or m>=60 or s<0 or s>=60:
    print ("error")
else :
    grad=round(h*30+m*0.5+s*(0.5/60),2)
    print(grad)

