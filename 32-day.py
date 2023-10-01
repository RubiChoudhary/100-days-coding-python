from itertools import permutations

s, k= input().split()
k= int(k)
permutations=sorted(permutations(s,k))

for perm in permutations:
    print(''.join(perm))


# Explanation

# All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.

#   Task
# You are given a string .
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

# Input Format
# A single line containing the space separated string  and the integer value .

  
# Sample Input

# HACK 2
# Sample Output

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
