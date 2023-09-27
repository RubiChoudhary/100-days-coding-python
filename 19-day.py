# butterfly pattern
n=int(input())
for i in range(0, n-2):
    for j in range(i+1):
        print("*", end=' ')
    for j in range(0, n-i-3):
        print(" ", end=' ')
    for j in range(0, n-i-3):
        print(" ", end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()
for i in range(0, n-2):
    for j in range(n-i-2):
        print("*", end=' ')
    for j in range(0,i):
        print(" ", end=' ')
    for j in range(1,i+1):
        print(" ", end=' ')
    for j in range(0, n-i-2):
        print("*", end=' ')
    print()


# it will print
# *         *
# * *     * *
# * * * * * *
# * * * * * *
# * *     * *
# *         *
