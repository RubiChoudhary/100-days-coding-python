num = int(input("Enter a number: "))
num_str = str(num)
sum = 0
for i in range(len(num_str)):
    sum = sum + int(num_str[i]) ** (i + 1)
    print(sum)
if sum == num:
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")
