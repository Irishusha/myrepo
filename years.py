years=int(input())
if years <=1582 :
    print("error")
else :
    if (years %4 == 0 and years%100 != 0) or years % 400 == 0 :
        print("366")
    else:
        print("365")
