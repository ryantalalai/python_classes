#Lab #7
#Date: 11/12/2021
# Ryan Talalai

class MinBinaryHeap:
    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        return self._heap[0]
    
    
    def _parent(self,index):
        try:
            if index <= 1:
                return None
            return self._heap[(index-2)//2]             # Formula for parent index in list
        except:                                         # Returns None if there is no index, instead of error
            return None

    def _leftChild(self, index):
        try:
            return self._heap[2*index-1]
        except:
            return None
    
    def _rightChild(self, index):
        try:
            return self._heap[2*index]
        except:
            return None
    
    def insert(self, item):
        self._heap.append(item)
        item_heap_index = len(self._heap)

        i = item_heap_index - 1
        while self._heap[(i-1)//2] >= self._heap[i] and i > 0:
            self._heap[(i-1)//2], self._heap[i] = self._heap[i], self._parent(i+1)
            i = (i-1)//2

    
    def deleteMin(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            root = self._heap[0]
            heap_index = len(self) - 1
            self._heap[0] = self._heap[heap_index]
            i = 0
            while True:                                           # Loops until it hits the break
                smallest_index = i
                right_index = 2*i+2
                left_index = 2*i+1
                if left_index <= heap_index and self._leftChild(i+1) < self._heap[smallest_index]:
                    smallest_index = left_index
                if right_index <= heap_index and self._rightChild(i+1) < self._heap[smallest_index]:
                    smallest_index = right_index
                if i == smallest_index:
                    break
                self._heap[i], self._heap[smallest_index] = self._heap[smallest_index], self._heap[i]
                i = smallest_index
            self._heap.pop()
            return root



def heapSort(numList):
    h = MinBinaryHeap()
    num = 0
    while num < len(numList):
        h.insert(numList[num])
        num += 1

    heap_sort = []
    num = 0
    while num < len(numList):
        smallest_num = h.deleteMin()
        heap_sort.append(smallest_num)
        num += 1

    return heap_sort