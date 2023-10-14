s=input()
upper=[]
lower=[]
even_digit=[]
odd_digit=[]

for i in s:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i.isdigit():
        if int(i) % 2==1:
            odd_digit.append(i)
        else:
            even_digit.append(i)
lower.sort()
upper.sort()
odd_digit.sort()
even_digit.sort()
rubi_sorted=''.join(lower+upper+odd_digit+even_digit)
print(rubi_sorted)
