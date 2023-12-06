# Finding Minimum and Maximum Element in an array
# METHOD-1

my_input = input().split()
element = []

for x in my_input:
    element.append(int(x))
if not element:
    print("Array is empty.")
else:
    element.sort()
    print("Sorted Array:", element)
    min_element = element[0]
    max_element = element[-1]
    print("Minimum Element:", min_element)
    print("Maximum Element:", max_element)

# output:-
# 4 2 5 5 1
# Sorted Array: [1,2,4,5,5]
# Minimum Element: 1
# Maximum Element: 5


# METHOD-2
element =[1,2,4,5,5]
if not element:
    print("Array is empty.")
else:
    element.sort()
    min_element = element[0]
    max_element = element[-1]
    print("Minimum Element:", min_element)
    print("Maximum Element:", max_element)
