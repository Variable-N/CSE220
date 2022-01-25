
def remove(source, validLength, index):
    if index >= validLength-1: print("Invalid Index")
    else:
        for i in range(index,validLength):
            source[i] = source[i+1]
    print(source)



a = [10,20,30,40,50,0,0,0] 
remove(a,6,1)
a = [10,20,30,40,50,0,0,0] 
remove(a,6,2)
a = [10,20,30,40,50,0,0,0] 
remove(a,6,3)
a = [10,20,30,40,50,0,0,0] 
remove(a,6,4)
a = [10,20,30,40,50,0,0,0] 
remove(a,6,5)
a = [10,20,30,40,50,0,0,0] 
remove(a,6,6)

source=[10,20,30,40,50,0,0]
remove(source,5,2)

