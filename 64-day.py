# Function to check if a turn is good
def is_good_turn(x, y):
    return x + y > 6

T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    if is_good_turn(X, Y):
        print("YES")
    else:
        print("NO")
