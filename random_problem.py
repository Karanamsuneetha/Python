import random
name=input("enter the list of names with comas separated")
name_list=name.split(",")
#print(name_list)
length=len(name_list)
random_choice=random.randint(0,length-1)
print(f"{name_list[random_choice]} will pay the bill")




