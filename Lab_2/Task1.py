class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

    
class MyList:
    def __init__(self,a= None):
        if a==None:
            self.head = None
        elif isinstance(a,list):
            head = None
            tail = None
            for i in a:
                node1 = Node(i,None)
                if head is None:
                    head = node1
                    tail = node1

                else:
                    tail.next = node1
                    tail =tail.next
            self.head = head
            
        elif isinstance(a,MyList):
            n=a.head
            head = None
            tail = None
            while n!=None:
                
                node1 = Node(n.element,None)
                if head==None:
                    head = node1
                    tail = node1

                else:
                    tail.next = node1
                    tail = node1
                n=n.next
            self.head = head
        
    def showList(self):
            if self.head== None:
                print("empty list")
            else:
                showing = " "
                show = self.head
                while(show!=None):
                    showing += str(show.element)+">"
                    show =  show.next
                print(showing)

    def isEmpty(self):
            if self.head!=None:
                return False
            else:
                return True

    def clear(self):
            while self.head!=None:
                head = self.head
                self.head=self.head.next
                head=None
        
    def insertElement(self,newElement,index=None):
        c = self.head
        while c!=None:
            if c.element==newElement:
                return
            c =c.next
        if index == None:
            node = Node(newElement,None)
            if self.head== None:
                self.head = node
                return
            else:
                tail = self.head
                while tail.next!=None:
                    tail=tail.next
                tail.next = node


            return
       
        size = 0  
        i = self.head
        while i!=None:
               i=i.next
               size+=1
        if index <0 or index > size:
            print("inavlid index")
            return
        else:
            if index == 0:
                node=  Node(newElement,self.head)
                node.next = self.head
                self.head = node
            else:
                node = Node(newElement,None)
                i = self.head
                c = 0
                while i!=None:
                    c+=1
                    if c==index:
                        break
                    i = i.next
                temp = i.next
                i.next=node
                node.next=temp

    def remove(self,deletekey):
        b = self.head
        if b!=None:
            if b.element == deletekey:
                self.head = b.next
                b = None
                return deletekey
            else:
                while b!=None:
                    if b.element==deletekey:
                        break
                    prev = b
                    b = b.next
                if deletekey==None:
                    return deletekey
                if b == None:
                    return deletekey
                prev.next = b.next
                b = None
                    
    def evenNum(self):
        even = MyList()
        i = self.head
        while i!=None:
            if i.element % 2 == 0:
                even.insertElement(i.element)
            i = i.next
        return even



    def find(self,findkey):
        search = self.head
        while search!=None:
            if search.element == findkey:
                return True
            search = search.next
        return False
    
    def reverse(self):
        temp = None
        new = self.head
        while new!= None:
            tail = new.next
            new.next = temp
            temp = new
            new = tail
        self.head = temp

    def sort(self):
        sorting = self.head
        index = None
        while sorting!=None:
            index = sorting.next
            while index!=None:
                if sorting.element > index.element:
                    temp = sorting.element
                    sorting.element = index.element
                    index.element = temp
                index = index.next
            sorting = sorting.next


    def sum(self):
        s = self.head
        sum = 0
        while s!=None:
            sum = sum+s.element
            s = s.next
        return sum

    def rotate(self,position,k):
        if position == "Right":
            for i in range(k):
                temp = None
                j = self.head
                while j.next.next!=None:
                    j = j.next
                temp = j.next
                j.next = None
            
            temp.next = self.head
            self.head = temp

        
        elif position == "left":
                temp = self.head
                self.head = self.head.next
                temp.next = None
                j = self.head
                while j.next!=None:
                    j=j.next
                j.next = temp
        else:
            print("wrong postion")

                
        


    
              
          
          

        
        


         

            
           

     
print("Task-1:")
print("Node class created, Mylist class created")    
print(" Task-2:")      
print("1. Constructor")
a = MyList()
b = MyList([1,2,3,4])
c = MyList(b)
print("2. def showList(self)")
a.showList()
b.showList()
c.showList()
print("3.  def isEmpty(self)")
print(a.isEmpty())
print(b.isEmpty())
print(c.isEmpty())
print("4. def clear(self)")
c.clear()
c.showList()
print("5. def insertElement(self, newElement)")
b.insertElement(6)
b.showList()
print("6. def insertElement(self, newElement, index)")
b.insertElement(2,3)
b.showList()
print("7. def remove(self, deletekey) ")
b.remove(4)
b.showList()
print(" Task-3:")      
print("1. def evenNum(self)")
c = b.evenNum()
c.showList()
print("2. def find(self,findkey):")
print(b.find(3))
print("3. def reverse(self):")
b.reverse()
b.showList()
print("4. def sort(self):")
b.sort()
b.showList()
print("5. def sum(self):")
print(b.sum())
print("6. def rotate(self,position,k)")
b.rotate('left',2)
