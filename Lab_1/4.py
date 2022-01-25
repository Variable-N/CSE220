def removeAll(source,size,element):
    count = 0
    for i in range(size):
        if source[i] == element:
            source[i] = 0
            count += 1
    if count == 0:
        print('No value found')
        return source
    else: 
        i = 0
        j = 0
        while i<len(source)-count:
            if source[i] == 0:
                j = i + 1
                while  j < len(source)-1 and source[j] == 0:
                    j += 1    
                source[i] = source[j]
                source[j] = 0
            i += 1
        return source
                


source=[10,2,2,2,2,2,30,2,50,2,4,0,0]
removeAll(source,11,2)
print(source)