class Queue(object):
    """Class implementation of a Queue"""
    def __init__(self):
        # list collection used to build internal representation
        self.items = []

    def isEmpty(self):
        # Check if queue is empty or not, and return boolean
        return self.items == []

    def enqueue(self, item):
        # Insert item at end of list, which is at index 0
        # O(n) runtime - depends on length of queue
        # Returns nothing
        self.items.insert(0, item)

    def dequeue(self):
        # Remove item from front of list, which is at index -1
        # O(1) runtime - constant
        # Returns popped item.  Modifies queue.
        return self.items.pop()

    def size(self):
        # Return number of items in queue as an int
        return len(self.items)
