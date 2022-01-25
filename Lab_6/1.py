def minIndexFinder(array,index,minIndex = None):
    if minIndex is None: minIndex = index
    if index == len(array): return minIndex
    if array[index] < array[minIndex]: minIndex = index
    return minIndexFinder(array, index+1, minIndex)

def sort_Selection (array,index=0):
    if index == len(array) - 1:
        return
    minIndex = minIndexFinder(array,index)
    array[index],array[minIndex] = array[minIndex],array[index]
    return sort_Selection(array,index+1)

a = [5,3,1,2,4]
print(a)
sort_Selection(a)
print(a)    