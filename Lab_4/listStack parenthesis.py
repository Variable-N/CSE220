class Node:
    def __init__(self,v,n):
        self.value = v
        self.next = n

class listStack:
    def __init__(self):
        self.head = None
    
    def push (self,element):
        if self.head is None:
            self.head = Node(element,None)
        else:
            newNode = Node(element,self.head)
            self.head = newNode
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.value
    
    def pop (self):
        if self.head is None:
            return None
        t = self.head
        self.head = self.head.next
        return t.value

def strIndex (string,item):
    c = 0
    for i in string:
        if i == item:
            return c
        c += 1
    return None


def parenthesisBalancing(equation):
    opening = "({["
    closing = ")}]"
    brackets = listStack()
    for i in equation:
        if i in opening:
            brackets.push(i)
        elif i in closing:
            if brackets.peek() == None:
                print("This equation is not correct.")
                print("At character # 1 '{}'- not opened.".format(i))
                return
            pop = brackets.pop()
            if closing[strIndex(opening,pop)] != i:
                print("This equation is not correct.")
                print("At character # {} '{}'- not closed.".format(strIndex(equation,pop)+1,pop))
                return
    if brackets.peek() != None:
        print("This equation is not correct.")
        while brackets.peek() != None:
            print("At character # {} '{}'- not opened.".format(strIndex(equation,brackets.peek())+1,brackets.pop()))
        return
    else:
        print("This equation is correct.")
        return


        
parenthesisBalancing("({[[1+2*(3/4)")
parenthesisBalancing("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
parenthesisBalancing("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
parenthesisBalancing("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
