a=[1,2,3,4]
b= [2,3,4,5,6]
for i in a:
    for j in b:
        if i<j:
            print('({},{})'.format(i,j))
