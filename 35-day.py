# Write Program to find the array type 
# Description Get an array as input from the user and check the type of the array, 
# whether it is odd, even or mixed type.
# Input Enter size of array: 3 
# Enter elements 1 3 5 
# Output Odd 
# Strictly follow the format of Input and Output Test Case 1 Test Case 2 Test Case 3 
# Input (stdin) 4 1 2 3 4 
# Output (stdout) Mixed


n=int(input())
arr=[]
print("elements: ")
for i in range(0,n):
    temp=int(input())
    arr.append(temp)
    
o=0
e=0
for i in range(0,n):
    if (arr[i]%2==1):
        o=o+1
    else:
        e=e+1
if (o==n):
    print("odd")
elif(e==n):
    print("even")
else:
    print("Mixed")
