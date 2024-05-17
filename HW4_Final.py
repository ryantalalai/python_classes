# HW4
# Date: 11/08/2021
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
            sorted_word = ''.join(sorted(value))
            initial_word = [value]
            dict = {sorted_word: initial_word}
            self.root = Node(dict)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        dict = node.value
        sorted_word = ''.join(sorted(value))
        initial_word = [value]
        dict1 = {sorted_word: initial_word}

        if sorted_word in dict:
            dict[sorted_word].append(value)
        else:
            keys = str(dict.keys())
            temp_lst = keys.split("'")
            key_node = temp_lst[1]

            if self._lessthan(sorted_word, key_node) == True:
                if(node.left==None):
                    node.left = Node(dict1)
                else:
                    self._insert(node.left, value)
            else:   
                if(node.right==None):
                    node.right = Node(dict1)
                else:
                    self._insert(node.right, value)
    
    def _lessthan(self, word1, word2):          # Helper function for _insert to determine which word is 'lessthan', or which comes alphabetically first
        words = [word1, word2]                  # Returns True if the first word comes before the second word
        words.sort()                            # Returns False Otherwise
        if words[0] == word1:
            return True
        else:
            return False


    def isEmpty(self):
        return self.root == None

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



class Anagrams:   
    def __init__(self, word_size):
        self.word_size = word_size
        self._bst = BinarySearchTree()


    def create(self, file_name):
        with open(file_name) as f:          # ensures the file closes after the file operation finishes 
            contents = f.read()             # reads the entire file, saving data in contents as string 

        words = contents.splitlines()
        num = 0
        while num < len(words):
            if len(words[num]) <= self.word_size and (words[num]).isalpha() == True:
                self._bst.insert(words[num])
            num += 1
        

    def getAnagrams(self, word):
        root = self._bst.root
        sorted_word = ''.join(sorted(word))

        while root != None:
            if sorted_word in root.value:
                return root.value[sorted_word]
            elif sorted_word < list(root.value.keys())[0]:          # Less than Node
                root = root.left
            else:                                                   # Greater than Node
                root = root.right
        return 'No match'