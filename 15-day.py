n= int(input())
ans=1
for i in range(0, n):
    for j in range(0, i+1):
        print(ans, end=' ')
        ans=ans+1
    print()
