weight=float(input("weight:"))
height=float(input("height:"))
bmi=weight/((height*100)**2)
if bmi>0:
    if bmi<18.5:
        print("u r under weight")
    elif 18.5<=bmi<24.9:
        print("u r in normal weight catogary")
    elif 25<=bmi<29.9:
        print("u r in over weight catogary")
    else:
        print("u r obess")
else:
    print("invalid value")
