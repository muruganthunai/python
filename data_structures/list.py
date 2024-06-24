#adding elements
a=['apple','banana','orange']
print(type(a))
a.append('pineapple')
print(a)
a.insert(2,'goa')
print(a)
b=[1,2,3,4]
a.extend(b)
print(a)

#deleting elements
a.pop(4)
print("popped",a)
a.remove(1)
print(a)
del a[-1]
print(a)
a.clear()
print(a)

#slicing
a=[12,14,14,16,15]
print(a.count(14))             #count
a.sort()                       #sort
print(a)
a.sort(reverse=True)           #reverse sort
print(a)
print(a[::-1])                 #reverse sorting using range
print(a)
print(a.index(15))             #index of the element
print(a[0])                    #initial value
print(a[-1])                   #final value
print(a[:-1])                  #printing upto final value
print(a[:3:2])                 #stop:3rd step:2
print(min(a))                  #minimum value
print(max(a))                  #maximum value
print(sum(a))                  #sum value
a=['baker','apple','cat']
print(a)
a.sort()                       #string sorting
print(a)
print(max(a))                  #maximum
print(min(a))                  #minimum