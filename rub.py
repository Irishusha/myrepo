k=int(input())
if k < 0 or k > 99:
    print("error")
else :
    if k == 1:
        print(k, " рубль")
    if k % 10 in [2,3,4]:
        print(k, " рубля")
    else :
        print(k, " рублей")