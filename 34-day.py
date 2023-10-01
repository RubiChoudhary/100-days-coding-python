# combinations_with_replacement

from itertools import combinations_with_replacement

s,k= input().split()
string=sorted(s)
k=int(k)
for i in combinations_with_replacement(string, k):
    print(''. join(i))


# Task

# You are given a string s.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

# Input Format

# A single line containing the string s and integer value  separated by a space

# Sample Input

# HACK 2
# Sample Output

# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK
