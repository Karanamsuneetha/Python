def reverse_array(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def rotate_array(arr,positions):
    n=len(arr)
    if n==0 or positions%n==0:
        return arr
    positions%=n
    reverse_array(arr,0,positions-1)
    reverse_array(arr,positions,n-1)
    reverse_array(arr,0,n-1)
    return arr
user_input=input("enter the array with commas")
array=[int(x) for x in user_input.split(',')]
positions=int(input("enter the number of positions"))
print("Original array:",array)
rotate_array(array,positions)
print('after rotation',array)