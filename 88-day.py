from itertools import combinations
word , length  = input().split()
for i in range(1, int(length)+1):
    for j in combinations(sorted(word), i):
        print (''.join(j))


# Input (stdin)
# HACK 2
# Expected Output
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
# Blog
