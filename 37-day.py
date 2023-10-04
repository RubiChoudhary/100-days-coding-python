def remove_duplicate(string):
    p = ""
    for char in string:
        if char not in p:
            p = p + char
    print(p)

def merge_the_tools(string, k):
    words = int(len(string) / k)
    for i in range(words):
        sus = string[(k * i):(k * (i + 1))]
        remove_duplicate(sus)
      
# Input (stdin)
# AABCAAADA
# 3
# Expected Output
# AB
# CA
# AD
