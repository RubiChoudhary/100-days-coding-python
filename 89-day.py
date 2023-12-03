    
num = [1, 2, 4, 5]
k = 5
sum1 = 0
summing =0
for i in range(1,k+1):
    summing   = summing + i 
print(summing)
for j in num:
    sum1 = sum1+j
    if summing != sum1:
        missing_number =summing - sum1
print("missing number",missing_number)

# missing number is 3
