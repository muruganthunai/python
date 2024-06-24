'''num=int(input("enter the number:"))
if num>1:
    devisor=2
    while devisor<num:
        if num%devisor==0:
            print("its not a prime number")
            break
        devisor+=1
    else:
        print("its a prime number")
else:
    print("its not a prime number")

a=input("enter sting:")
b=list(a)
i=0
while i<len(b):
    if i==4:
        i+=1
        continue
    print(b[i])
    i+=1'''


a=[15,16,17,18,19,20,21,22,23,24,25]
g=0
for i in a:
    if i>=20:
        print("values greater than 20",i,end=" ")
        g+=i
print('\n',g)