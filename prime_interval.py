lower_num=int(input("enter the lower value"))
upper_num=int(input("enter the upper value"))
print("the lower number and upper number are:")
for num in range(lower_num,upper_num+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)