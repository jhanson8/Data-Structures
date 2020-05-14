"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

'''
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        if len(self.storage) >= 1:
            return self.storage.pop(0)'''

class Queue:
    class Node:

        def __init__(self, element, _next):
                self.element = element
                self._next = _next

    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0 

    def enqueue(self, element):
        new = self.Node(element, None)
        if self.is_empty():
            self.head = new
        else:
            self.tail._next = new 
        self.tail = new 
        self.size += 1 

    def dequeue(self):
        if self.is_empty():
            return None
        result = self.head.element 
        self.head = self.head._next
        self.size -= 1 
        if self.is_empty():
            self.tail = None 
        return result 





