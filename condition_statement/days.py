a=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

b=int(input("enter the number(1 to 7):"))
if b in range(1,8):
    if b==1:
        print(a[0])
    elif b==2:
        print(a[1])
    elif b==3:
        print(a[2])
    elif b==4:
        print(a[3])
    elif b==5:
        print(a[4])
    elif b==6:
        print(a[5])
    else:
        print(a[6])

else:
    print("please enter the right values between 1 to 7")