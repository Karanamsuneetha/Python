def set_min(A):
    mini=float('inf')
    for num in A:
        if num < mini:
            mini=num
    return mini

def set_max(A):
    maxi=float('-inf')
    for num in A:
        if num > maxi:
            maxi=num
    return maxi

user_input = input("enter the input array with commas")
A = [int(x) for x in user_input.split(',')]
print("minimum element is: ",set_min(A))
print("maximum element is: ",set_max(A))

