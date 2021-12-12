a=int(input())
b=int(input())
c=int(input())
max, min, mid = a,a,a
if b >= max:
    max = b
if c >= max :
    max = c
if b <= min :
    min = b
if c <= min :
    min = c
z=a+b+c
mid=z-max-min
print(max)
print(min) 
print(mid)
