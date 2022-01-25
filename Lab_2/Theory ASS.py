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
            for i in range(len(a)):        
                newNode = Node(a[i],None)
                if head is None:
                    head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = tail.next
            self.head = head

    def showList(self):                             # Prints the entire list
        if self.head == None:                       # Prints Empty List if the list has no nodes
            print("Empty list")
        else:
            current = self.head
            string = ''
            while(current != None):
                string += str(current.value) + " --> "
                current = current.next
            print(string)
    
def printDuplicate (head):    
    i = head
    j = head
    while i is not None:
        j = i.next
        while j is not None:
            if i.value == j.value:
                print(i.value)
                return
            j = j.next
        i = i.next
    print("No duplicate found")
    return

def remove_multiple_of_five(head):
    i = head
    j = head
    while i is not None:
        if i.value%5 == 0:
            j.next = i.next
        j = i.next
        i = i.next
    i = head
    while i is not None:
        print(i.value,end = " > ")
        i = i.next
    return  head


a = myList([-1,1,1,5,6])
remove_multiple_of_five(a.head)
