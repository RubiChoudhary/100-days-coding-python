from itertools import permutations

s, k = input().split()
k = int(k)
perm = list(permutations(sorted(s), k))

for p in perm:
    print(''.join(p))


# Input (stdin)
# HACK 2
# Expected Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
