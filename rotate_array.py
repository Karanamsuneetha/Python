def rotate_array(arr,positions,direction='left'):
    n=len(arr)
    if n==0:
        return arr
    positions%=n
    if direction=='left':
        return arr[positions:]+arr[:positions]
    elif direction=='right':
        return arr[-positions:]+arr[:-positions]
    else:
        raise ValueError("Invalid direction.Use 'left' or 'right'.")
user_input=input("enter the array with commas")
array=[int(x) for x in user_input.split(',')]
positions=int(input("enter the number of positions"))
print("Original array:",array)
print("left rotated array:",rotate_array(array,positions,'left'))
print("right rotated array:",rotate_array(array,positions,'right'))