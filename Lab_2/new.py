class Node:             #NODE CLASS
    def __init__(self,element,next):
        self.element = element
        self.next = next

class myList:                                   #My List Class
    def __init__(self,a = None):                    # Constructor
        if a is None:    
            self.head = None
        elif isinstance(a,list):
            lastValue = True
            for i in range (len(a)-1,-1,-1):
                if lastValue:
                    lastValue = False
                    newNode = Node(a[i],None)
                else:
                    newNode = Node(a[i],newNode)
            self.head = newNode
        


    def showList(self):                             # Prints the entire list
        if self.head == None:
            print("EMPTY LIST")
            return
        i = self.head
        while i != None :
            print(i.element,end = " > ")
            i = i.next
        print()
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def clear(self):
        self.head = None
    
    def insert(self, newElement, index = None):
        i = self.head
        size = 0
        while i != None :
            if i.element == newElement:
                print("New element already exist.")
                return
            i = i.next
            size += 1
        if index == None:
            #INDEX CHARA CODE TA KORBI
            pass
        elif index >= 0 and index < size:
            
            #VALID INDEX ER CODE
            pass
        else:
            print("INVALID INDEX")
            return


array = [1,2,3,4]
linkedList = myList(array)
linkedList.showList()
linkedList.clear()
linkedList.showList()