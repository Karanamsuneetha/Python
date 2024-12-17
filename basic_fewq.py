#divisibility of 3
#number=int(input("enter the number"))
#if number%3==0:
#    print("it is divisible")
#else:
#    print("not divisible")

# age related question
#age=int(input("enter the age"))
#if age>18:
#    print("old enough")
#else:
#    print("to young")

#display the greeting if both names are same
#name=input("enter your name")
#name1=input("enter the another name")
#if str(name)==str(name1):
 #   print("good morning have a nice day")
#else:
    #print("")

#largest number among two integers
#number1=int(input("enter the first number"))
#number2=int(input("enter the second number"))
#if number1>number2:
 #   print(f"{number1} number1 is greater")
#elif number1==number2:
#    print(f"{number1} and {number2} are equal")
#else:
    #print(f"{number2} number2 is greater")

#dispalying vowel or not
#alphabet=str(input("enter the letter"))
#vowel=('a','e','i','o','u')
#if alphabet.lower() in vowel:
 #   print("True")
#else:
 #   print("False")

#eligible for voting
#age=int(input("enter the age"))
#if age<18:
 #   print("to young to vote")
#else:
 #   print("old enough to vote")
#value = expression_if_true if condition else expression_if_false ,format for ternary condition
#votable="to young" if age<18 else "old enough" using ternary condition
#print("Votable status:",votable)

#password checking
original_password = "suneetha"
password = input("Please enter your password: ")
if original_password == password:
    print("Correct! The password you entered matches the original password.")
else:
    print("Incorrect password.")
