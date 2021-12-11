from math import sqrt
figure=str(input())
if figure == "треугольник" :
    a=int(input())
    b=int(input())
    c=int(input())
    if a>0 and b>0 and c>0 :
        p=(a+b+c)/2
        s=sqrt(p*(p-a)*(p-b)*(p-c))
        print(s)
    else :
       print("error") 
elif figure == "прямоугольник" :
    a=int(input())
    b=int(input())
    if a> 0 and b> 0 :
        s=a*b
        print(s)
    else :
        print("error")
elif figure == "круг" :
    r=int(input())
    if r> 0 :
        s=3.14*r**2
        print(s)
    else :
      print("error")  
else :
    print("error")