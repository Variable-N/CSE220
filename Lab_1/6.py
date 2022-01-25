def arrayMaker(n):
    ar = [0]*n*n
    x = 0
    seg = 1
    for i in range(n*n):
        if x >= n-seg: 
            ar[i] = n - x
        x += 1
        if x == n:
            x = 0
            seg += 1
        
    return ar

print(arrayMaker(4))