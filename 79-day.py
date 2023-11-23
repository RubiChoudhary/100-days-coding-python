class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        
        first_str = strs[0]
        last_str = strs[-1]
        common_prefix = ""
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                break
        
        return common_prefix



# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
