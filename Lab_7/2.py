class HashTable:
    def __init__(self):
        self.hashArray = [None]*10
        self.count = 0
        
    def index(self,element):
        sum = 0
        count = 0
        for i in element:
            if i >= '0' and i <= '9':
                sum += int(i)
            elif i not in ['A','E','I','O','U','a','e','i','o','u']:
                count += 1
        return (count*24+sum)%9

    def resize(self):
        newArray = [None]*(len(self.hashArray)+5)
        for i in range(len(self.hashArray)):
            newArray[i] = self.hashArray[i]
        self.hashArray = newArray

    def push(self,element):
        self.count += 1
        if self.count > len(self.hashArray):
            self.resize()
        if self.hashArray[self.index(element)] is not None:
            self.linearProbing(element)
        else:
            self.hashArray[self.index(element)] = element
        
    def linearProbing(self,element):
        i = self.index(element) 
        c = 0
        while self.hashArray[i] is not None and c != len(self.hashArray):
            i = (i+1)%len(self.hashArray)
            c += 1
        self.hashArray[i] = element

#Test Statement
c = HashTable()
array = ["BZDYBD","ZRDYNYZ","YERBBDZR","ZBTRDS","BTZRS","ZTBRSD","TBZRTRS","NDTSRYR","FAASDDE"]
for i in array:
    c.push(i)
print(c.hashArray)