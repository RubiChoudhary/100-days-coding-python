n=int(input())
for i in range(0, n):
    for j in range(0, n-i):
        print(n-j, end=' ')
    print()

# it will print
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3 
# 5 4
# 5
