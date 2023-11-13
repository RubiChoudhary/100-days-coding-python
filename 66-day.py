# Sample Input 1:
# 2000
# 2.2
# 4
# Sample Output 1:
# 176
# Explanation of Sample Input 1:
# The input is principal=2000, rate=2.2 and time=4.
# So Simple interest=Principal*rate*time/100 hence 
# answer is 2000*2.2*4/100=176

from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
principal =int(input())
rate_of_interest =float(input())
time =int(input())
simple_interest = (principal*rate_of_interest*time)/100
print(int(simple_interest))
