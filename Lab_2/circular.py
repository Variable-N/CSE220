class Node:             #NODE CLASS
    def __init__(self,value,next):
        self.value = value
        self.next = next

class myList:                                   #My List Class
    def __init__(self,a = None):                    # Constructor
        if a is None:                               # Creates empty list
            self.head = None
        elif isinstance(a, list):                   # Creates list from Array
            head = None
            tail = None
            lastNode = None
            for i in range(len(a)):        
                newNode = Node(a[i],None)
                if head is None:
                    head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = tail.next
                lastNode = newNode
            self.head = head
            lastNode.next = self.head

    def showList(self):                             # Prints the entire list
        if self.head == None:                       # Prints Empty List if the list has no nodes
            print("Empty list")
        else:
            current = self.head
            string = ""
            first = True
            while current is not self.head or first:
                first = False
                string += str(current.value) + " --> "
                current = current.next
            print(string)

    def insert(self, value, index):
        if index == 0:
            i = self.head
            while i.next is not self.head:
                i = i.next
            newNode = Node(value,self.head)
            i.next = newNode
            self.head = newNode
            return self.head
        else:
            count = 1
            i = self.head
            while i.next is not self.head:
                if count == index:
                    break
                count += 1
                i = i.next
            newNode = Node(value,i.next)
            i.next = newNode
            return self.head
            

cir1 = myList([1,2,3,4])
cir1.insert(0,5)
cir1.showList()