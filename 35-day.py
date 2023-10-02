# Write Program to check if two arrays are the same or not.
# Description Get two arrays as the input from the user and check whether it is the same or not.
# Sample Input 
# Enter the size of first array: n1 
# Enter the size of second array: n2 
# Accept elements of array 1
# Accept elements of array 2 
# Sample Output 
# Same Strictly follow the format of Input and Output Test Case 1 Test Case 2 Test Case 3 
# Input (stdin) 3 3 1 2 3 1 2 3 
# Output (stdout) Same



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
