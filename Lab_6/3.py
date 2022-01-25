class Node:             #NODE CLASS
    def __init__(self,value,next):
        self.value = value
        self.next = next

class singlyLinkedList:                                       # My List Class
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

    def swap(self,x):                             # Swaps value x to its next values. such as 0>1>2 to 0>2>1
        prev = None
        cur = self.head
        if self.head.value == x:                  # Handles if x is First element
            newHead = cur.next
            cur.next = cur.next.next
            newHead.next = cur
            self.head = newHead
            return
        
        while cur.next is not None:               # If x is not the first element. also handles if x is the last value and then it does not swap :)
            if cur.value == x:
                prev.next = cur.next
                prev = prev.next
                cur.next = cur.next.next
                prev.next = cur
                return
            first = False
            prev = cur
            cur = cur.next    

def sort(singlyLinkedList):                               # Sorts the list using bubble sort algorithm
    current = singlyLinkedList.head
    swap = True
    while swap:
        swap = False
        current =  singlyLinkedList.head
        while current.next is not None:
            if current.value > current.next.value:
                swap = True
                singlyLinkedList.swap(current.value)
            else: 
                current = current.next

a = singlyLinkedList([7, 4, 2, 5, 3, 1, 6])
sort(a)
a.showList()
                