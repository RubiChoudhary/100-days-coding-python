total_set = int(input())

for i in range(total_set):
    setA = int(input())
    A = set(map(int, input().split()))
    setB = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))
