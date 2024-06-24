a=(input("enter the number:"))
b=list(a)
lent=len(b)
c=(int(b[0])**lent)+(int(b[1])**lent)+(int(b[2])**lent)
d=str(c)
if a==d:
    print("it's an armstrong number")

else:
    print("it's not an armstrong number")
