n=int(input())
num=97
for i in range(0, n):
    for j in range(i+1):
        print(chr(num+i), end=' ')
    print()

# it will print
# a
# b b
# c c c
# d d d d
# e e e e e
