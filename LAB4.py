# LAB4
# Date: 10/08/2021
# Ryan Talalai


########################################
# 
# Collaboration Statement: 
#      I referred to:
#       [1] https://docs.python.org/3/library/copy.html
#     in order to complete the replicate method
#      
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node

        elif new_node.value <= self.head.value:
            new_node.next = self.head
            self.head = new_node

        elif new_node.value >= self.tail.value:
            self.tail.next = new_node
            self.tail = new_node
            

        else:
            current = self.head
            while current.next.value < new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

                


    def replicate(self):
        import copy                                #[1]
        lst = copy.deepcopy(self)                  #[1] Creating a dupilicate object to modify and return
        
        if lst.isEmpty():
            return None
        else:
            current = lst.head
            while current.value < lst.tail.value:
                if current.value < 0 or isinstance(current.value, float):
                    lst.add(current.value)
                else:
                    i = 1
                    while i < current.value:
                        lst.add(current.value)
                        i += 1
                current = current.next
            
            if lst.tail.value <= 0 or isinstance(lst.tail.value, float):
                lst.add(lst.tail.value)
            else:
                i = 1
                while i < lst.tail.value:
                    lst.add(lst.tail.value)
                    i += 1

        return lst

    def removeDuplicates(self):
        if self.head != None:
            current = self.head.next
            previous = self.head
            count = 0
            while count < len(self):
                if current.value == previous.value:
                    previous.next = current.next
                    current = current.next
                else:
                    previous = current
                    current = current.next
                count += 1
