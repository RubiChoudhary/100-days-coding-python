# Kadane's algorithm
N = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Check if the array has at least one element
if N > 0:
    start = arr[0]
    end = arr[0]

    # Iterate over the array
    for i in range(1, N):
        # Update max_ending_here
        end = max(arr[i], end + arr[i])
        # Update max_so_far
        start = max(start, end)

    print("Maximum subarray sum:", start)
else:
    print("Array size should be at least 1.")
