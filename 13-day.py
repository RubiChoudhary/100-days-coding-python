n= int(input())
for i in range(0,n):
    for j in range(0, n-i-1):
        print("#", end=' ')
    for j in range(2*i+1):
        print("*", end=' ')
    for j in range(0, n-i-1):
        print("#", end=' ')
    print()
for i in range(0,n):
    for j in range(0, n-i-1):
        print("#", end=' ')
    for j in range(2*i+1):
        print("*", end=' ')
    for j in range(0, n-i-1):
        print("#", end=' ')
    print()
for i in range(0, n):
    for j in range(0, n-2):
        print("#", end=' ')
    for j in range(0, 3):
        print("*", end=' ')
    for j in range(0, n-2):
        print("#", end=' ')
    print()
    
    
