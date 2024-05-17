# HW5
# Date: 11/20/2021
# Ryan Talalai

########################################
# 
# Collaboration Statement: 
#      I referred to:
#       [1] https://docs.python.org/3/library/functions.html#map
#     in order to complete the __hash__ method
#
########################################


class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class ContentItem:
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return f'CONTENT ID: {self.cid} SIZE: {self.size} HEADER: {self.header} CONTENT: {self.content}'

    __repr__=__str__

    def __eq__(self, other):
        if isinstance(other, ContentItem):
            return self.cid == other.cid and self.size == other.size and self.header == other.header and self.content == other.content
        return False

    def __hash__(self):
        return (sum(map(ord,self.header)))%3            # [1]



class CacheList:
    def __init__(self, size):
        self.head = None
        self.maxSize = size
        self.remainingSpace = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return 'REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}'.format(self.remainingSpace, self.numItems, listString)  

    __repr__=__str__

    def __len__(self):
        return self.numItems
    
    def put(self, content, evictionPolicy):
        if content.size > self.maxSize:                                                 # Error Case 1
            return "Insertion not allowed"
        elif self.__contains__(content.cid) is not None:                                # Error Case 2
            return f"Content {content.cid} already in cache, insertion not allowed"
        while self.remainingSpace < content.size:
            if evictionPolicy == "mru":
                self.mruEvict()
            elif evictionPolicy == "lru":
                self.lruEvict()

        self.remainingSpace -= content.size
        self.numItems += 1

        node_obj = Node(content)
        node_obj.next = self.head
        self.head = node_obj
        if self.head.next is None:
            self.tail = self.head
        
        return f"INSERTED: {content}"

    

    def __contains__(self, cid):
        if len(self) == 0:
            return None
        previous_pointer = None
        head_pointer = self.head
        while head_pointer.value.cid != cid and head_pointer.next != None:
            previous_pointer = head_pointer
            head_pointer = head_pointer.next
        if head_pointer.value.cid == cid:
            if self.head != head_pointer:
                if previous_pointer:
                    previous_pointer.next = head_pointer.next
                head_pointer.next = self.head
                self.head = head_pointer
            return self.head.value


    def update(self, cid, content):
        content_item = self.__contains__(cid)
        if content_item == None:
            return 'Cache miss!'
        self.remainingSpace = self.remainingSpace + content_item.size
        if content.size > self.remainingSpace:
            self.remainingSpace = self.remainingSpace - content_item.size
            return 'Cache miss!'
        else:
            self.head.value = content
            self.remainingSpace = self.remainingSpace - content.size
            return f"UPDATED: {content}"


    def mruEvict(self):
        if len(self) == 0:
            return None
        node = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        self.remainingSpace += node.value.size
        self.numItems -= 1

    
    def lruEvict(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            node = self.head
            self.tail = self.head = None
            self.remainingSpace += node.value.size
            self.numItems -= 1
            return None
        previous_pointer = None
        head_pointer = self.head
        while head_pointer.next != None:
            previous_pointer = head_pointer
            head_pointer = head_pointer.next
        if previous_pointer != None:
            previous_pointer.next = None
        self.tail = previous_pointer
        self.remainingSpace += head_pointer.value.size
        self.numItems -= 1

    
    def clear(self):
        self.remainingSpace = self.maxSize
        self.head = None
        self.tail = None
        self.numItems = 0
        return 'Cleared cache!'


class Cache:
    def __init__(self):
        self.hierarchy = [CacheList(200), CacheList(200), CacheList(200)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__


    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    
    def insert(self, content, evictionPolicy):
        cache_update = self.hierarchy[content.__hash__()].put(content, evictionPolicy)
        if cache_update == None:
            return "Cache miss!"
        else:
            return cache_update


    def __getitem__(self, content):
        cache_update = self.hierarchy[content.__hash__()].__contains__(content.cid)
        if cache_update == None:
            return "Cache miss!"
        else:
            return cache_update



    def updateContent(self, content):
        cache_update = self.hierarchy[content.__hash__()].update(content.cid, content)
        if cache_update == None:
            return "Cache miss!"
        else:
            return cache_update