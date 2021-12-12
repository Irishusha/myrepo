a=int(input())
b=int(input())
c=int(input())
max, min, mid = a,a,a
if b >= max:
    max = b
  #  mid = a
if c >= max :
    max = c
   # mid = a   
if b <= min :
    min = b
if c <= min :
    min = c
    #mid = b
z=a+b+c
mid=z-max-min
print(max)
print(min) 
print(mid)
