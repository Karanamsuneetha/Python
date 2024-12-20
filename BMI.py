weight=float(input("enter the weight in kg"))
height=float(input("enter the height in meters"))
BMI=float(weight)/float(height**2)
#BMI=int(int(weight)/float(height**2))
print(BMI)
#print(round(674.1012,1))
if BMI<18.5:
    print(f"Your weight is{BMI} and your underweight")
elif BMI<25:
    print(f"Your weight is{BMI} and your normal range")
else:
    print(f"Your weight is{BMI} and your overweight")
