p=int(input("the principle is:"))
t=int(input("the time period is:"))
r=float(input("the rate of interest is:"))
A= p+(pow((1+r/100),t))
ci=A-p
print("the compound interest of the give values are:",ci)
