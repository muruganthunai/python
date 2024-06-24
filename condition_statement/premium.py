rate=int(input("total amount:"))
pre=input("do u have premium subscription?(yes/no):")
if pre=='yes' or (rate>50 and rate>0):
    print("Delivery charge is free, congratulations!")
elif pre=='no' or (rate<50 and rate>0):
    print(f"your bill amount {rate} + 10$ delivery charge: {rate+10}$ ")
else:
    print("please reconcider the values u have given")