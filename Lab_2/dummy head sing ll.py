class Node:             #NODE CLASS
    def __init__(self,value,next):
        self.value = value
        self.next = next

class myList:                                   #My List Class
    def __init__(self,a = None):                    # Constructor
        if a is None:                               # Creates empty list
            self.head = Node(None,None)
        elif isinstance(a, list):                   # Creates list from Array
            self.head = Node(None,None)
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
            self.head.next = head

    def showList(self):
        i = self.head.next
        while i is not None:
            print(i.value,end = " > ")
            i = i.next
        print()

def remove_multiple_of_five(head):
    i = head.next
    j = head
    while i is not None:
        if i.value % 5 == 0:
            j.next = i.next
            i = None
            i = j.next
        else:
            j = j.next
            i = i.next
    return head

def sum_of_two_list(list1,list2):
    list1Value = ""
    list2Value = ""
    i = list1.head.next
    while i is not None:
        list1Value += str(i.value)
        i = i.next
    i = list2.head.next
    while i is not None:
        list2Value += str(i.value)
        i = i.next
    list1Value = int(list1Value)
    list2Value = int(list2Value)
    list3Value = str(list1Value + list2Value)
    newArray = [0]*len(list3Value)
    index = 0
    for i in list3Value:
        newArray[index] = i
        index += 1
    return myList(newArray)


    



l1 = myList([4,5,3])
l2 = myList([9,5,2])
l3 = sum_of_two_list(l1,l2)
l3.showList()

