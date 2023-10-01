from itertools import combinations

s, k = input().split()
k = int(k)

s = ''.join(sorted(s))

for i in range(1,k + 1):
    for combo in combinations(s, i):
        print(''.join(combo))

# Task

# You are given a string s .
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

# Input Format

# A single line containing the string s and integer value k separated by a space.
# Sample Input

# HACK 2
# Sample Output

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
