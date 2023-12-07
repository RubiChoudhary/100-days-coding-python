A= input().split()
start = 0
end =len(A)-1
while start < end: 
	A[start], A[end] = A[end], A[start] 
	start += 1
	end -= 1
print("Reversed list is") 
print(A) 

# output:-
# 2 6 3 7 5
# Reversed output is : 5 7 3 6 2
