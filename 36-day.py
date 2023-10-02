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

def arrays(arr1, arr2, n1, n2):
    count = 0
    arr1.sort()
    arr2.sort()
    for i in range(0,n1):
        if(arr1[i] == arr2[i]):
            count = count + 1
        print(count)
    return count

n1 = int(input("Enter the size of first array: "))
n2 = int(input("Enter the size of second array: "))
arr1 = []
arr2 = []
print("Enter the elements of first array: ")
for i in range(0,n1):
    temp = int(input())
    arr1.append(temp)
print("Enter the elements of second array: ")
for i in range(0,n2):
    temp = int(input())
    arr2.append(temp)

if(arrays(arr1, arr2, n1, n2) != n1):
    print("Not Same")
else:
    print("Same")
