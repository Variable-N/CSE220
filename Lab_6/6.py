def binarySearch(array,value,mini = 0, maxi = None):
    if maxi is None:
        maxi = len(array)
    mid = (maxi+mini)//2
    if array[mid] == value:
        return mid
    if array[mid] > value:
        return binarySearch(array,value,mini,mid)
    else:
        return binarySearch(array,value,mid,maxi)


array = [1,2,3,4,5]
print(binarySearch(array,2))
