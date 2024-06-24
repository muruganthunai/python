a={'apple','banana'}
print(a)
a.add(51)
print("adding a value to the set:",a)
a.update(['orange',22,25,26])
print("using update adding multiple values",a)
a.discard(51)
print("discarded value(51)",a)
a.pop()
print("to remove a random value(pop)",a)
a.remove(26)
print("to remove a particular value",a)
del a

#superset,subset,disjoint

a={1,2,3,4,5,6}
b={7,8,9}
print("subset",b.issubset(a))             #subset
print("superset",a.issuperset(b))         #superset
print("disjoint",a.isdisjoint(b))         #disjoint

#list to set

x=[1,2,3,4,5]
y=set(x)
print ("list to set",y)

#string list to set

z=['aravindh']
print("string list to set",set(z))

#tuple to set

h=('madam')
s=set(h)
print("tuple to set",s)

#set operators

s1={1,2,3,4,5,6,7,8}
s2={1,3,5,7,9,10,11,12}
print("union",s1|s2)             #union
print(s1.union(s2))
print("intersection",s1&s2)      #intersection
print(s1.intersection(s2))
print("differerence",s1-s2)      #difference
print(s1.difference(s2))
print("sym_difference",s1^s2)    #symmetric difference
print(s1.symmetric_difference(s2))