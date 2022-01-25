def checkBalance(source):
    i = 0
    divider = 1
    while i < len(source)-1:
        s1 = 0
        s2 = 0
        for j in range(len(source)):
            if j< divider:
                s1 += source[j]
            else:
                s2 += source[j]
        if s1 == s2:
            return True
        i += 1
        divider +=1
    return False

a =  [10, 3, 1, 2, 10]
print(checkBalance(a))

