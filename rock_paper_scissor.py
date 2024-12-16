import random
user_choice=int(input("enter the value b/w 0 and 2"))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number:you lose")
else:
    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(computer_choice)
    if user_choice==computer_choice:
       print("the game is draw.")
    elif computer_choice>user_choice:
       print("You lose.")
    elif user_choice >computer_choice:
       print("You win.")
    elif computer_choice==0 and user_choice==2:
       print("You lose.")
    elif computer_choice==2 and user_choice==0:
       print("You win.")

