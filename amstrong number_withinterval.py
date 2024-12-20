start=int(input("enter the start value"))
end=int(input("enter the end value"))
print(f"the armstrong number b/w {start} and {end}: ")
for num in range(start,end+1):
    num_digits=len(str(num))
    sum_of_powers = 0
    temp=num
    while temp>0:
        digit=temp%10
        sum_of_powers+=digit**num_digits
        temp//=10
    if num==sum_of_powers:
        print(num)