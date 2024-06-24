bill=int(input("enter the units:"))
if bill>=0:
    if bill<=100:
        print("the amount is:",5*bill)
    elif bill>100 and bill<=200:
        print("the amount is:",(7.50*(bill-100))+500)
    else:
        print("the amount is:",(10*bill))
else :
    print("invalide number")