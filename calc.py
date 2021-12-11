# put your python code here
a=float(input())
b=float(input())
oper=str(input())

if oper=="+":
  print(a+b)
elif oper=="-":
  print(a-b)
elif oper=="*":
  print(a*b)
elif oper == "/":
  if b != 0 :
    print(a/b)
  else :
    print("Деление на 0!") 
elif oper == "mod" :
  if b != 0 :
    print(a%b)  
  else :
    print("Деление на 0!") 
elif oper == "div" :
  if b != 0 :
    print(a//b) 
  else :
    print("Деление на 0!") 
elif oper == "pow" :
  #  if b>=0 :
  print(a**b)
elif b == 0 :
    print("Деление на 0!")
