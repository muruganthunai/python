a=[1,2,3,4,5,6]
numbers=a[0]
numbers1=a[0]
for num in a:
    if num>numbers:
        numbers=num
    else:
        num<numbers1
        numbers1=num
print("the largest number is:",numbers)
print("the lowest number is:",numbers1)