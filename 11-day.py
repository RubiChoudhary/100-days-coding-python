n= int(input())
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end=' ')
    for j in range(0, i+1):
        print(j%2, end=' ')
    for j in range(1, i+1):
        print((i+j)%2, end= ' ')
    print()

     #     0
     #    010
     #   01010
     #  0101010
     # 010101010
