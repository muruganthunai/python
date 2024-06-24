a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=int(input("enter the number:"))
e=int(input("enter the number:"))


if (a >= b and a >= c) and (a>=d and a>=e) :
    if b>c>d>e:
        print(f'{b} is the second greatest')
    elif c>b>d>e:
        print(f'{c} is the second greatest')
    elif d>c>b>e:
        print(f'{d} is the second greatest')
    else:
        print(f'{e} is the second greatest')
        

elif (b>=a and b>=c) and (b>=d and b>=e):
    if a>c>d>e:
        print(f"{a} is the second greatest")
    elif c>a>d>e:
        print(f"{c} is the second greatest")
    elif d>a>c>e:
        print(f"{d} is the second greatest")
    else:
        print(f'{e} is the second greatest')

elif (c>=a and c>=b) and (c>=d and c>=e):
    if a>b>d>e:
        print(f"{a} is the second greatest")
    elif b>a>d>e:
        print(f"{b} is the second greatest")
    elif d>a>b>e:
        print(f"{d} is the second greatest")
    else:
        print(f'{e} is the second greatest')

elif (d>=a and d>=b) and (d>=c and d>=e):
    if a>b>c>e:
        print(f"{a} is the second greatest")
    elif b>a>c>e:
        print(f"{b} is the second greatest")
    elif c>a>b>e:
        print(f"{c} is the second greatest")
    else:
        print(f'{e} is the second greatest')

else:
    if (e>=a and e>=b) and (e>=c and e>=d):
        if a>b>c>d:
            print(f"{a} is the second greatest")
        elif b>a>c>d:
            print(f"{b} is the second greatest")
        elif c>a>b>d:
            print(f"{c} is the second greatest")
        else:
            print(f'{d} is the second greatest')

    
