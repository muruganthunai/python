year=int(input("year:"))
if (year%4==0 and year%400==0) or year%100 !=0:
    print("its the leap year")
else:
    print("its not a leap year")