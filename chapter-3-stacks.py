class Stack(object):
    """Implementing a Stack class"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # returns a boolean - True if empty, False otherwise
        return self.items == []

    def push(self, item):
        # Add item to top of stack.  Modifies stack.
        self.items.append(item)

    def pop(self):
        # Remove item from top of stack.  Modifies stack. Returns popped item.
        return self.items.pop()

    def peek(self):
        # Peek at top item but do not remove. Does not modify stack.
        return self.items[-1]

    def size(self):
        # Return number of items in stack as an int.
        return len(self.items)
