class arrayStack:
    def __init__(self):
        self.stack = []
        self.pointer = -1
    
    def push (self,element):
        self.stack += [element]
        self.pointer += 1
    
    def peek(self):
        if self.pointer == -1:
            return None
        return self.stack[self.pointer]
    
    def pop (self):
        if self.pointer == -1:
            return None
        temp = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return temp


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
    brackets = arrayStack()
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



parenthesisBalancing("1+2*(3/4)")
parenthesisBalancing("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
parenthesisBalancing("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
parenthesisBalancing("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")

