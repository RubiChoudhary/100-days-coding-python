n = int(input())
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(0, n):
    for j in range(0,n-2,1):
        print(" ", end=' ')
    for j in range(0,3,1):
        print("*", end=' ')
    print()

# just checking
