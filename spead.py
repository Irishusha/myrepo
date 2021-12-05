spead=float(input())
if spead <= 0:
    print("error")
else:
    if spead <= 7.8 :
        print("0")
    elif 7.8 <= spead <= 11.2:
        print("1")
    elif 11.2 <= spead <= 16.4:
        print("2")
    elif spead >= 16.4:
        print("3")