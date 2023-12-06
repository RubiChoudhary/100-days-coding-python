def read_1d_array(size):
    array = []
    for i in range(size):
        value = int(input(f"Enter element at position {i + 1}: "))
        array.append(value)
    return array
size = int(input("Enter the size of the array: "))

my_array = read_1d_array(size)

print("The entered 1D array is:", my_array)
