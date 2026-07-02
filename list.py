# Node Definitions
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Print Linked List
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

#Insert at beginning
def insert_beginning(head, value):
    new_node = ListNode(value)
    new_node.next = head
    return new_node

#Insert at end
def insert_end(head, value):
    new_node = ListNode(value)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

 # Delete at beginning
def delete_beginning(head):
    if head is None:
        return None
    return head.next

# Delete from end
def delete_end(head):
    if head is None or head.next is None:
        return None
        current = head
        while current.next.next:
            current = current.next
            current.next = None
            return head

# Search an element
def search(head, target):
    current = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False

# Find Length

def lenth(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

head = None

#Insert at end
head = insert_end(head,10)
head = insert_end(head,20)
head = insert_end(head,30)
head = insert_end(head,40)
print_list(head)
                    
