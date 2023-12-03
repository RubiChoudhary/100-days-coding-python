from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

product_result = product(a, b)

for x, y in product_result:
    print(f'({x}, {y})', end=' ')


# Input (stdin)
# 1 2
# 3 4
# Expected Output
# (1, 3) (1, 4) (2, 3) (2, 4)
