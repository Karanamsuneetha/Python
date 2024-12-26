num=int(input("enter the number"))#6
sump=0
for i in range(1,num): #i=1,2 ,3
    if num%i==0:# 6%1==0, 6%2==0,0
        sump+=i#sump=1, sump=1+2=3 sump=3+3=6
if sump==num:
    print("it is a perfect number")
else:
    print("not a perfect number")


