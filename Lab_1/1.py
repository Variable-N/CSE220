
def shiftLeft(source,k):
    for i in range (0,len(source)-k):
        source[i] = source[i+k]
    while(k!=0):
        source[len(source)-k] = 0
        k -= 1


a = [10,20,30,40,50,60]
shiftLeft(a,1)
print(a)
a = [10,20,30,40,50,60]
shiftLeft(a,2)
print(a)
a = [10,20,30,40,50,60]
shiftLeft(a,3)
print(a)
a = [10,20,30,40,50,60]
shiftLeft(a,4)
print(a)
a = [10,20,30,40,50,60]
shiftLeft(a,5)
print(a)
a = [10,20,30,40,50,60]
shiftLeft(a,6)
print(a)

