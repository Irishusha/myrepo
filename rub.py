# put your python code here
k=int(input())
if k < 0 or k > 99:
  print("ошибка")
elif k in [11,12,13,14]:
    print(k, "рублей")
elif k % 10 == 1:
  print(k, "рубль")
else :
  if k % 10 in [2,3,4]:
    print(k, "рубля")
  else :
    print(k, "рублей")