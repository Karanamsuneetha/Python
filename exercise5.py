size=input("enter the size of the pizza(s/m/l)")
bill=0
if size=='s'or size=='S':
    bill=bill+100
    print("small size pizza is 100rs")
elif size=='m' or size=='M':
    bill=bill+200
    print("medium size pizza is 200rs")
else:
    bill=bill+300
    print("large size pizza is 300rs")
add_pepporoni=input("enter the pepporoni size y/n")
if add_pepporoni=='y'or add_pepporoni=='Y':
    if size=='s' or size=='S':
        bill=bill+30
        print("pay 30rs")
    else:
        bill = bill + 50
        print("pay extra 50rs")
extra_cheese=input("do you want extra cheese Y/N")
if extra_cheese=='y' or extra_cheese=='Y':
    bill += 20
print(f"the total bill is {bill}")

