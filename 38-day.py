class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax(arr: list, n: int) -> Pair:
    minmax = Pair()

    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

# Input the array size
arr_size = int(input("Enter the size of the array: "))

# Input the array elements
arr = []
for i in range(arr_size):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

minmax = getMinMax(arr, arr_size)
print("Minimum element is", minmax.min)
print("Maximum element is", minmax.max)
