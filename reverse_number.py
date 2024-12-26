num=int(input("enter the number"))
temp=num
reverse=0
while num>0:# 123>0, 12>0,1>0
    remainder=num%10 #3 is extracted ,12%10=2 1%10=1
    reverse=(reverse*10)+remainder #3,32
    num=num//10 #123//10=12 , 12//10=1 1//10=0
print("The Given number is {} and Reverse is {}".format(temp, reverse))
