n=int(input())
if 0<= n<=1000:
    if n in [11,12,13,14] :
        print(n, "программистов")
    elif n % 100 in [11,12,13,14] :
        print(n, "программистов")
    elif n % 10 == 1:
        print(n,"программист")
    elif n % 10 in [2,3,4]:
        print(n, "программиста")
    else :
        print(n,"программистов")
else :
    print("error")
