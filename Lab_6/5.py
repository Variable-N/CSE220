class Node:             #NODE CLASS
    def __init__(self,value,next,prev):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyList:
    def __init__(self,a):
        if len(a) == 0:
            self.head = None
        else:
            self.head = Node(a[0],None,None)
            prv = self.head
            for i in range(1,len(a)):
                newNode = Node(a[i],None,prv)
                prv.next = newNode
                prv = newNode
                
    def showList(self):
        if self.head is None:
            print("Empty List")
            return
        tail = self.head
        string = ""
        while tail is not None:
            string += "-< "+ str(tail.value)+" >-"
            tail = tail.next
        print(string)


def sort_insertionX(doublyList):
    i = doublyList.head
    while i.next is not None:
        j = i.next
        while j is not None and j.value < j.prev.value:
            j.value, j.prev.value = j.prev.value, j.value
            j = j.prev
            if j.prev is None:
                break
        i = i.next

                    
a = DoublyList([5,4,2,1,6,7,3])
a.showList()
sort_insertionX(a)
a.showList()