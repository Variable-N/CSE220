class Node:             #NODE CLASS
    def __init__(self,value,next,prev):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyList:
    def __init__(self,a):
        self.head = Node(None,None,None)
        tail = self.head
        for i in range(len(a)):
            newNode = Node(a[i],None,None)
            tail.next = newNode
            newNode.prev = tail
            newNode.next = self.head
            self.head.prev = newNode
            tail = tail.next
        
    def showList(self):
        if self.head.next is self.head:
            print("Empty List")
            return
        tail = self.head.next
        string = "-< Head >-"
        while tail is not self.head:
            string += "-< "+ str(tail.value)+" >-"
            tail = tail.next
        print(string)

    def has(self,val):
        tail = self.head.next
        while tail is not self.head:
            if tail.value == val:
                return True
            tail = tail.next
        return False

    def insert(self,newElement,index = None):
        if self.has(newElement):
            print("New element already exists in the list. Insertion aborted.")
            return
        if index is None:
            newNode = Node(newElement,None,None)
            tail = self.head.prev 
            tail.next = newNode
            newNode.prev = tail
            newNode.next = self.head
            tail = newNode
            return
        i = self.head
        firstHead = True
        c = 0
        validIndex =False
        while i is not self.head or firstHead:
            firstHead = False
            if c == index:
                validIndex = True
                break
            i=i.next
            c+=1
        if validIndex:
            newNode = Node(newElement,i.next,i)
            i.next = newNode
            newNode.next.prev = newNode
            return
        else:
            print("Invalid Index. Insertion aborted.")

    def remove(self,index):
        i = self.head.next
        c = 0
        validIndex =False
        while i is not self.head:
            if c == index:
                validIndex = True
                break
            i=i.next
            c+=1
        if validIndex:
            i.prev.next = i.next
            i.next.prev = i.prev
            i = None
            return
        else:            
            print("Invalid Index")
    
    def removeKey(self,deleteKey):
        i = self.head.next
        while i is not self.head:
            if i.value == deleteKey:
                i.prev.next = i.next
                i.next.prev = i.prev
                i = None
                return deleteKey
            i = i.next
        print("Value not found.")
        return deleteKey

def insertBefore (head, elem, newElement):
    i = head.next
    while i is not head:
        if i.value == elem:
            newNode = Node(newElement,i,i.prev)
            i.prev.next = newNode
            i.prev =  newNode
            return
        i = i.next


a = DoublyList([1,2,3,4,5,6,7,8,9,10])
insertBefore(a.head,5,50)
a.showList()