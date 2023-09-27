n=int(input())
for i in range(0, n):
    num=97
    for j in range(0,i+1):
        print("%c" %(num), end=' ')
        num+=1
    print()

# it will print
# a
# a b
# a b c 
# a b c d
# a b c d e
