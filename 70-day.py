def solution():
  # Write code here
  size = int(input())
  elements = input().split()
  longest_palindrome = ""
  max_length = 0
  for element in elements:
      if element == element[::-1] and len(element) > max_length:
          longest_palindrome = element
          max_length = len(element)
  print(longest_palindrome)

  pass


# Write Program to find longest palindrome in an array
# Description

# Get an array as the input from the user and find the longest palindrome in that array. Strictly follow the input and output format.
# Input
# Enter the size of array
# 3

# Enter the elements of array
# 121  10456  1000001

# Output
# 1000001
