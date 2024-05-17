# Lab #5
# Date: 10/22/2021
# Ryan Talalai


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
 
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    def mirror(self):
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        




    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False




    def _mirrorHelper(self, node):       

        if node == None:
            return None
        else:
            self._mirrorHelper(node.left)
            self._mirrorHelper(node.right)

            temp = node.left
            node.left = node.right
            node.right = temp

            return node
        


    @property
    def getMin(self): 
        minimum = self.root

        while minimum.left != None:
            minimum = minimum.left

        return minimum



    @property
    def getMax(self): 
        maximum = self.root

        while maximum.right != None:
            maximum = maximum.right

        return maximum



    def __contains__(self,value):
        root = self.root
        while root != None:
            if root.value == value:
                return True
            if root.value > value:
                root = root.left
            else:
                root = root.right
        


    def getHeight(self, node):
        height = 0
        while node.right != None or node.left != None:
            while node.right != None:
                node = node.right
                height += 1
            while node.left != None:
                node = node.left
                height += 1
        return height





