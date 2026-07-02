class Stack:
    def __init__(self):
        self.stack = []

    # Push
    def push(self, value):
        self.stack.append(value)

    # Pop
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    # Peek/Top
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    # Check if empty
    def is_empty(self):
        return len(self.stack) == 0

    # Search
    def search(self, value):
        return value in self.stack

    # Display
    def display(self):
        print(self.stack)


# Example
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("Stack elements:")
s.display()

print("Top element:", s.peek())

print("Popped element:", s.pop())

print("After pop:")
s.display()

print("Search 20:", s.search(20))
print("Is Stack Empty?", s.is_empty())