number= int(input("enter the number"))
if number==0 and number==1:
    print(number,"is not a prime number")
elif number>1:
    for i in range(2,number):
        if number%i==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")

else:
    print(number,"is not a prime number")