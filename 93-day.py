# Duplicate values in a list 
nums = input().split()
for i in nums:
    if nums!=i:
        print(True)
        break
    else:
        print(False)

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
