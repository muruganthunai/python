marks=int(input("enter the number:"))
if marks>=0 and marks<=100:
    if marks>=90 and marks<=100:
        print("u r an 'A' grade")
    elif marks>=80 and marks<=89:
        print("u r an 'B' grade")
    elif marks>=70 and marks<=79:
        print("u r an 'C' grade")
    elif marks>=60 and marks<=69:
        print("u r an 'D' grade")
    else:
        print("u r an 'F' grade")
else:
    print("enter the valid marks")