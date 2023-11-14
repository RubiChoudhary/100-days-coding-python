def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

n = int(input())

arr = list(map(int, input().split()))
result = remove_duplicates(arr)
for element in result:
    print(element, end=" ")


# Write Program to remove duplicate elements in an array

# Description
# Get an array as input from the user and then remove all the duplicate elements in that array.
# Strictly follow the input and output format.
# Input
# Enter the size of array
# 5

# Enter the elements of array
# 35  35  45  60  60
# Output
# 35 45 60
