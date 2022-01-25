#Task 1
def factorial(n):
    if n == 1: return 1
    return n*factorial(n-1)

print(factorial(5))

#Task 2
def fibonacci (n):
    if n == 1: return 0
    if n == 2: return 1
    sum = fibonacci(n-1) + fibonacci(n-2)
    return sum

print(fibonacci(10))

#Task 3

def printArray (a):
    if len(a) == 0: 
        print("None")
        return
    if len(a) == 1: 
        print(a[0])
        return
    print(a[0],"\b,",end = "")
    newArray = [0]*(len(a)-1)
    c = 0
    for i in range(len(a)):
        if i == 0: continue
        else: 
            newArray[c] = a[i]
            c += 1

    printArray(newArray)

printArray([1,2,3,4,5,6])

#Task 4

def decimalToBinary (n,stri=""):
    if n == 0 :
        if stri == "" :
            return '0'
        else:
            return stri
    if n%2 == 0:
        stri = '0' + stri
        return decimalToBinary(n//2,stri)
    else:
        stri = '1' + stri
        return decimalToBinary(n//2,stri)

print(decimalToBinary(512))

#Task 5

def power (n,m):
    if m == 1:
        return n
    return n * power (n,m-1)

print(power(2,2))

#Task 6

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

def sumList(head,sum=0):
    if head is None:
        return sum
    else:
        sum+= head.value
        return sumList(head.next,sum)


a = myList([1,2,3,4,5,6,7,8,9,10])
print(sumList(a.head))

#Task 7

def printList(head):
    if head is None:
        return
    else:
        printList(head.next)
        print(head.value)
        return
printList(a.head)