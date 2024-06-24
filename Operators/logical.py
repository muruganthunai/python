print(bin(8))
print(int('1010000',2))
a=50
print("AND OPERATOR:",a>100 and a<75)          #AND
print("OR OPERATOR: ",a>100 or a<75)            #OR
print("NOT OPERATOR:",not(a>100 and a<75))     #NOT

#operator symbols

x=40
y=20
x1=(bin(x))
y1=(bin(y))
print(x1,"\n",y1)
print(x & y)             #AND
print(x | y)             #OR
print(x ^ y)             #XOR
print(~(x))              #NOT
print(x>>2)              #RIGHT SHIFT
print(y<<2)              #LEFT SHIFT
