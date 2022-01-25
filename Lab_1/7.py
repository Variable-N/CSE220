def maxBunchCount(source):
    count = 1
    res = 1
    for i in range(1,len(source)):
        if source[i] == source[i-1]:
            count += 1
        else:
            count = 1
        if res < count:
            res = count
    return res 

print(maxBunchCount([1,1,2, 2, 1, 1,1,1]))