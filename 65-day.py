# Sample Input 1:
# 7
# 1 3 7 9 11 12 45
# 3
# Sample Output 1:
# 1
# Explanation of sample output 1:
# nums = [1, 3, 7, 9, 11, 12, 45],
# The index of element '3' is 1.
# Hence, the answer is '1'.


# Sample Input 2:
# 7
# 1 2 3 4 5 6 7
# 9
# Sample Output 2:
# -1
# Explanation of sample output 2:
# nums = [1, 2, 3, 4, 5, 6, 7],
# Element '9' doesn't exist.
# Hence, the answer is '-1'.


def search(nums: [int], target: int):
    # write your code logic !!
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

    
n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())
print (search(arr, target))
