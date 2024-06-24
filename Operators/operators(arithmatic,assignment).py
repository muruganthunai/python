def io():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=input("choose the arithmatic operator(add,sub,div,mod,floor,power):")
    if c=="add":
        add(a,b)

    elif c=="sub":
       sub(a,b)
    
    elif c=="mul":
       mul(a,b)
    
    elif c=="div":
       div(a,b)

    elif c=="mod":
       mod(a,b)

    elif c=="floor":
       floor(a,b)

    elif c=="power":
       power(a,b)

def add(a,b):
    a+=b
    print("Addition value:",a)

def sub(a,b):
    a-=b
    print("substaction value:",a)

def mul(a,b):
    a*=b
    print("multiplication value:",a)

def div(a,b):
    a/=b
    print("aivition value:",a)

def mod(a,b):
    a%=b
    print("moaulo value:",a)

def floor(a,b):
    a//=b
    print("floor aivision value:",a)

def power(a,b):
    a**=b
    print("power value:",a)


io()
