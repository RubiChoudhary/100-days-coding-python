from itertools import product
A = list( input().split())
B = list(input().split())

# Compute cartesian product
result = list(product(A, B))

# Sort the result
result.sort()

# Print the result
for item in result:
    print(item, end=' ')
