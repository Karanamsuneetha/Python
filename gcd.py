num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
def gcd_function(num1,num2):
    while num2:
        num1,num2=num2,num1%num2
    return num1
gcd=gcd_function(num1,num2)
gcd_abc=gcd_function(gcd,num3)
print("GCD of three numbers are:{}".format(gcd_abc))
