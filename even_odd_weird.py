number=int(input("enter the number"))
if number%2==0:
    if number>=2 or number<=5:
        print("not weird")
    elif number>=6 or number<=20:
        print("weird")
    else:
        print("not weird")
else:
    print("weird")
