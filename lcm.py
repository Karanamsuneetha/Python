def lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm
a=int(input("enter the first value"))
b=int(input("enter the second value"))
print(f"the lcm of a,b is",lcm(a,b))