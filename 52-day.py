items = set(input().split())
N=int(input())
output=True
for i in range(0,N):
    items2 = set(input().split())
    if not items2.issubset(items):
        output=False
    if len(items2)>=len(items):
        output = False
print(output)
