n = int(input())  # Read the number of elements
L = list(map(int, input().split()))  # Read the list of integers

# Step 1: Separate non-zero values and count the zeros
non_zero_values = [x for x in L if x != 0]  # List of non-zero values
zero_count = L.count(0)  # Count the number of zeros

# Step 2: Print non-zero values
for value in non_zero_values:
    print(value, end=" ")

# Step 3: Print the zeros at the end
for _ in range(zero_count):
    print(0, end=" ")

