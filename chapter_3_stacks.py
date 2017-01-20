class Stack(object):
    """Implementing a Stack class"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # returns a boolean - True if empty, False otherwise
        return self.items == []

    def push(self, item):
        # Add item to top of stack.  Modifies stack.
        # O(1) runtime - constant time
        self.items.append(item)

    def pop(self):
        # Remove item from top of stack.  Modifies stack. Returns popped item.
        # O(1) runtime - constant time
        return self.items.pop()

    def peek(self):
        # Peek at top item but do not remove. Does not modify stack.
        return self.items[-1]

    def size(self):
        # Return number of items in stack as an int.
        return len(self.items)


######################################################################


def parentheses_checker(symbol_string):
    """Function to check if parenthese are balanced"""
    s = Stack()

    # No reason to assume otherwise at the start
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


#######################################################################


def is_balanced(symbol_string):
    """Function to check if all symbols are balanced"""
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    """Helper function to assist with symbol matching"""
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)
