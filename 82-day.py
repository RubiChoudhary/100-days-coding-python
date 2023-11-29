def power(num):
    if num <1:
        return 0
    elif num == 1:
        print(1)
        return 1
    else:
        prev = power(num//2)
        curr = prev*2
        print(curr)
        return curr
        
power(48)


# output:-
# 1
# 2
# 4
# 8
# 16
# 32
