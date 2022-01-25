
def shiftRight(source,k):
    for i in range (len(source)-1, k-1, -1):
        source[i] = source[i-k]
    for i in range(k):
        source[i] = 0


a = [10,20,30,40,50,60] 
shiftRight(a,1)
print(a)
a = [10,20,30,40,50,60] 
shiftRight(a,2)
print(a)
a = [10,20,30,40,50,60] 
shiftRight(a,3)
print(a)
a = [10,20,30,40,50,60] 
shiftRight(a,4)
print(a)
a = [10,20,30,40,50,60] 
shiftRight(a,5)
print(a)
a = [10,20,30,40,50,60] 
shiftRight(a,6)
print(a)

