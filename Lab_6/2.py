array = [7,4,2,5,3,1,6]

def sort_insertionR(array,i=0):
    if i == len(array)-1:
        return
    if array[i] > array[i+1]:
            j = i+1
            print(array)
            while j != 0 and array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
                j -= 1
    sort_insertionR(array,i+1)
    

def sort_insertion(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            j = i+1
            print(array)
            while j != 0 and array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
                j -= 1
                
            
sort_insertionR(array)
print(array)