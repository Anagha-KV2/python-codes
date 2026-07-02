class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addTwoNumbers(l1, l2):
    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10

        current.next = Node(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next

# Number 342 represented as 2 -> 4 -> 3
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

# Number 465 represented as 5 -> 6 -> 4
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

result = addTwoNumbers(l1, l2)

print("Result:")
printList(result)