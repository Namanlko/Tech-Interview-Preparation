# Problem 1: Leap Year: Check if year is leap year.

y = int(input("Enter Year:"))

if y%4 == 0:
    if y%100 == 0:
        if y%400 == 0:
            print(y,"is a Leap Year")
        else:
            print(y,"is not a Leap Year")
    else:
        print(y,"is a Leap Year")
else:
    print(y,"is not a Leap Year")