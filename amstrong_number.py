num=int(input("enter the number"))
num_digits=len(str(num))
#print(num_digits)
sum_of_digits=sum(int(digit)**num_digits for digit in str(num))
#print(sum_of_digits)
if num==sum_of_digits:
    print("Armstrong number")
else:
    print("not an armstrong number")
