day=input("day:")
age=int(input("age:"))
week_days=['monday','tuesday','wednesday','thursday','friday']
week_end=['saturday','sunday']
if day in week_days:
    if age<18:
        if age>0:
            print("the price is: $12")
        else:
            print("enter the valide age")
    else:
        print('the price is: $15')

elif day in week_end:
    if age<18:
        if age>0:
            print("the price is: $15")
        else:
            print("enter the valide age")
    else:
        print('the price is: $20')
else:
    print("enter the valid day")


    