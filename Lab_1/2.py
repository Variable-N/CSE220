
def rotateLeft(source,k):
    i = 0
    while i<k:
        temp = source[0]
        for j in range(len(source)-1):
           source[j] = source[j+1]
        source[len(source)-1] = temp
        i += 1





a = [10,20,30,40,50,60]
rotateLeft(a,1)
print(a)
a = [10,20,30,40,50,60]
rotateLeft(a,2)
print(a)
a = [10,20,30,40,50,60]
rotateLeft(a,3)
print(a)
a = [10,20,30,40,50,60]
rotateLeft(a,4)
print(a)
a = [10,20,30,40,50,60]
rotateLeft(a,5)
print(a)
a = [10,20,30,40,50,60] 
rotateLeft(a,6)
print(a)



