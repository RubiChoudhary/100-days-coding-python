n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        for c in range(i,0,-1):
            print(j,end=" ")
    print()

# it will print
# 3 3 3 2 2 2 1 1 1
# 3 3 2 2 1 1
# 3 2 1
