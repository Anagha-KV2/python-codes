class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoLists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next

def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next

# List 1: 1 -> 3 -> 5
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

# List 2: 2 -> 4 -> 6
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

merged = mergeTwoLists(l1, l2)

print("Merged List:")
printList(merged)