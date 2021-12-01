name=input("Ваше имя:")
print("Привет, ", name , "!")
age = int(input("Сколько вам лет?"))
height = float(input("Ваш рост:"))
weight = float (input ("Ваш вес в кг :"))
if age <10 or height<=0 or height>3 or weight<=0 or weight>500:
    print("Введены не верные данные!")
else:
    bmi = round(weight/height**2,2)
    print("Ваш индекс массы тела: ", bmi)
    if bmi<18.5: 
      description ="недостаточной массой тела."
    elif bmi<25:
      description ="нормальной массой тела."
    elif bmi <30:
      description ="избыточной массой тела."
    else:
      description ="ожирением."
    print("Вы относитесь к группе с ", description)
