'''choose=input("enter the datatype(int/str):")
if choose=='int': 
    a=int(input("enter the starting number:"))
    b=int(input("enter the ending number:"))
    for i in range(a,b+1):
        print (i)

else:
    if choose=='str':
        c=input("enter the string:")
        for i in c:
            print(i)
    else:
        print("invalide input")
x=[1,2,3,4]
y=0
for i in x:
    y+=i
    print(y)
x=[13,30,26,25,11,68]
for i in x:
    if i%2==0:
        print(i)
a="PyTHoN LaNGUagE"
x=0
y=0
z=0
for i in a:
    if i.isupper():
        x+=i.count(i)
        print(i,end=" ")
for i in a:
    if i.islower():
        y+=i.count(i)
        print(i,end=' ')
for i in a:
    if i.isspace():
        z+=i.count(i)
    
        
print("\nthe upper case:",x)
print("the lower case:",y)
print("the special charecter:",z)

for i in range(0,6):
    for j in range(i):
        print(' * ',end="")
    print()

for i in range(5,0,-1):
    print(' * '*i)

for i in range(5):
    for j in range(i,5):
        print(j,end="")
    print()

#break

for i in range(11):
    print(i)
    if i==7:
        break

# continue

for i in range(11):
    if i==7:
        continue
    print(i)

# pass

for i in range(11):
    if i==7:
        pass
    print(i)

a='aravindh'
for i in a:
    if i==a[4]:
        break
    print(i)'''
x=input("enter a string:")
for i in range(len(x)):
    if i>=6:
        break
    print(x[i])