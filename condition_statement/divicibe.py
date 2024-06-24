n=int(input("enter the number:"))
if n%2==0 and n%3==0:
    print("the given number is divicible by both 2&3")
elif n%2==0 or n%3==0:
    if n%2==0:
        print("the number is divicible by 2")
    else:
        print("the number is divicible by 3")
else:
    print("its not divicible by both")

