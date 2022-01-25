
n = 5
m = 5
array1 = [1 ,1 ,2, 2, 5]
array2 = [3, 1 ,4 ,1, 5]
string = ""
# for i in range(n):
#     array1[i] = int(input())
for i in range(m):
    #array2[i] = int(input())

    count = 0
    high = n-1
    low = 0
    given = array2[i]
    while low <= high:
        mid = (high+low)//2
        if array1[mid] < given:
            low = mid
            count = mid
            if low +1 == high:
                count = high
                if array1[high] <= given:
                    count+=1
                break
        elif array1[mid] == given:
            if mid + 1 != len(array1):
                if array1[mid+1] == given:
                    low = mid + 1
                    count = mid + 1
                else:
                    count = mid+1
                    break
            else:
                count = mid + 1
                break
        else:
            high = mid+1
            if low + 1 == mid and mid + 1 == high:
                if given < array1[0]:
                    count = 0
                else:
                    count += 1
                break
    string += str(count)+" "
            


print(string)


