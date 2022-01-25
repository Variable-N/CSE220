def Intersection (cir1,start_1,size_1,cir2,start_2,size_2):
    index1 = start_1
    index2 = start_2
    if len(cir1)>len(cir2): tempArray = [0]*len(cir1)
    else: tempArray = [0]*len(cir2)
    tempIndex = 0
    for i in range(size_1):
        index2 = start_2
        for j in range(size_2):
            j = j
            if cir1[index1] == cir2[index2] :
                tempArray[tempIndex] = cir1[index1]
                tempIndex += 1
            index2 = (index2+1)%len(cir2)
        index1 = (index1+1)%len(cir1)
    linArray = [0]*tempIndex
    for i in range(tempIndex):
        linArray[i] = tempArray[i]
    return linArray

print(Intersection([40,50,0,0,0,10,20,30],5,5,[10,20,5,0,0,0,0,0,5,40,15,25],8,7))

