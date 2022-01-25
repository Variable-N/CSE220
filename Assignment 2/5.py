#     5(A)
def patternA(n):
    if n == 0:
        return
    patternA(n-1)
    for i in range(1,n+1):
       print(i,end="")
    print()
    return
patternA(9)

#     5(B)

def patternB(n,max=None, first = True):
    if first:
        max = n
    if n == 0:
        return
    patternB(n-1,max,False)
    for i in range(max-n):
        print(" ",end = "")
    for i in range(1,n+1):
       print(i,end="")
    print()
    return

patternB(9)