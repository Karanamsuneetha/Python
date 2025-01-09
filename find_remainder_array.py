def find_remainder(arr,len,n):
    product=1
    for i in range(len):
        product=product*arr[i]
    return product%n
user_input=input("enter the array with commas")
array=[int(x) for x in user_input.split(',')]
len=len(array)
n=int(input("enter the value"))
print(find_remainder(array,len,n))