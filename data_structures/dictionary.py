a={'name':'aravindh','age':22,'ethnicity':'india','ph.no':7010442730}
a.update({'father name': 'Masanam','mother name':'Muppudathi','sister name':'jayanthi'})
print("updated items:",a)
a.popitem()
print("removing last element:",a)
a.pop('ethnicity')
print ("removing the paticular item ('ethnicity')",a)
a['age']=23
print("replacing a value of the particular key",a)
print("values of dictionary 'a':",a.values())
print("keys of dictionary 'a':",a.keys())
print("entier keys and values of dictionary 'a':",a.items())
print("printing a particular item (name):",a['name'])
b=a.copy()
print("copied values from dict a",b)

# converting list to dictionary

c=['aravindh','shankar','naga','lakshmi']
d=dict.fromkeys(c)
print ("converting list into dictionary:",d)
x=['rajee','masanam']
y=['aravindh','muppudathi']
z=dict(zip(x,y))
print("converting 2 lia=sts into a dictionary",z)
d['aravindh'],d['shankar'],d['naga'],d['lakshmi']=22,22,22,22
print(d)
