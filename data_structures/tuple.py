a=(1,2,3,'aravindh','naga')
print(a)
print("type",type(a))
print("length",len(a))
b=list(a)
print("converted into list",b)
b.append('shankar')
print("append",b)
b.pop(0)
print('pop',b)
c=[5,6,7,8]
b.extend(c)
print("extended:",b)
b.clear()
print ("clearing",b)
d=tuple(b)
print("converted into tuple",d)

#converted into set

e=set(a)
print("converted into set",e)
e.add(143)
print("add",e)
e.remove(1)
print("remove",e)
e.update(['orange','apple'])
print("update",e)
f=tuple(e)
print("converted into tuple",f)