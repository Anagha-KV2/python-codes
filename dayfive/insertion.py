class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Enqueue (Insertion)
    def enqueue(self, value):
        self.stack1.append(value)

    # Dequeue (Deletion)
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            print("Queue is Empty")
            return

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # Display Queue
    def display(self):
        queue = self.stack2[::-1] + self.stack1
        if not queue:
            print("Queue is Empty")
        else:
            print("Queue:", queue)


q = QueueUsingStacks()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        q.enqueue(value)
        print("Element inserted successfully")

    elif choice == 2:
        item = q.dequeue()
        if item is not None:
            print("Deleted element:", item)

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")