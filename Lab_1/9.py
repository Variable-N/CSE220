def Palindrome (cir,start,size):
    sIndex = start
    lIndex = (start+size-1)%len(cir)
    for i in range(size//2):
        if cir[sIndex] != cir[lIndex]:
            return False
    return True

print(Palindrome([30,20,10,0,0,10,20,30],5,6))