def reverse_string(n):
    reversed_string=""
    for char in n:
        reversed_string=char+reversed_string
    return reversed_string
output_string=input("enter the string")
reversed=reverse_string(output_string)
print(reversed)
