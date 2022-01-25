class keyIndex:
    def __init__(self,array):
        mx = None
        mn = None
        for i in range(len(array)):
            if mx is None or mx < array[i]:
                mx = array[i]
            if mn is None or mn > array[i]:
                mn = array[i]
        self.k = [0]*(mx-mn+1)
        self.center = mn*-1     # self.Center is the index where value 0 will sit, for example [-2,-1,0,1] , here 0 is in index no 2. so self.center will be 2.
                                # For all positive case like, [3,4,5,6], 0 is absent, but if 3 is in 0 no index, then 0 will be in -3 index(if negative index was possible)
                                # so, self.center will be -3 .      0  ,  1,  2   ,[3,4,5,6]
                                #                            -3    -2   -1    0,1,2,3
                                # This will be memory efficient for those cases where minimum value will be higher. 
                                # For example, [23214,23123,21311], in this case we dont have to create a array of length 23215.
        for i in array:
            self.k[self.center+i] += 1
        print(self.k)
    def search(self,value):
        index =value+self.center
        if value < (-1*self.center) or value > (-1*self.center) + len(self.k)-1:  #Checking if the value we need to find is outside of [min,....,max],if yes then False
            return False
        if self.k[index] > 0 :
            return True
        else:
            return False

    def sort(self):
        sum = 0
        for i in self.k:
            sum += i
        sortedArray = [0]*sum
        j=0
        for i in range(len(self.k)):
            x = self.k[i]
            while x!=0:
                sortedArray[j] = (-1*self.center)+i
                j += 1
                x -= 1

        return sortedArray    

#TEST STATEMENT
c = keyIndex([105,104,102,101,100,-25])
print(c.search(3))
print(c.sort())