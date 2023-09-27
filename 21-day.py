n=int(input())
num=97
for i in range(0, n):
    for j in range(i+1):
        print(chr(num), end=' ')
        num+=1
    print()


# it will print
# a
# b c
# d e f
# g h i j
# k l m n o
