n = int(input())

for i in range(0,n):
    for j in range(0,i):
        print(" ", end=' ')
    for j in range(0,1):
        print("*", end=' ')
    for j in range(1, n-i):
        print(" ", end=' ')
        
    for j in range(0, n-i-2):
        print(" ", end=' ')
    for j in range(0, n-i-1):
        if(i+j==n-2):
            print("*", end=' ')
    print()
for i in range(0,n-1):
    for j in range(0,n-i-2):
        print(" ", end=' ')
    for j in range(0,1):
        print("*", end=' ')
    for j in range(1,i+1):
        print(" ", end=' ')
    for j in range(0, i+1):
        print(" ", end=' ')
    for j in range(0,1):
        print("*", end=' ')
    print()
