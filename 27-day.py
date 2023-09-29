n = int(input())

for i in range(0,2*n):
    for j in range(0,2*n):
        if i==4 or j==4 :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

