def valueAche(arr,start,end,val):
    for i in range(start,end):
        if arr[i] != 0 and arr[i] == val:
            return True
    return False

def repetation(source):
    count = [0]*len(source)
    countIndex = 0
    for i in range(len(source)-1):
        if not valueAche(source,0,i,source[i]):
            for j in range(i+1,len(source)):
                if source[i] == source[j]:
                    count[countIndex] += 1
            countIndex += 1
                
    for i in range(len(count)):
        if valueAche(count,i+1,len(count),count[i]):
            return True
    return False

print(repetation([1,2,2,3,5,5,4]))
