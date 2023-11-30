#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    spelling = s.split()
    
    capitalized_words = []
    for word in spelling:
        capitalized_words.append(word.capitalize())
    
    capitalize_name = ' '.join(capitalized_words)
    return capitalize_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



# output
# input:- rubi choudhary
# output:- Rubi Choudhary
