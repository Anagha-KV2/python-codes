class ListNode:
    def__init__(self, val=0):
    self.val = val
    self.next = None
    def insert_beginning(head, value):
        new_node = ListNode(value)
        new_node.next = head
        return new_node
head=None
head = insert_end(head,10)
head = insert_end(head,20)
head = insert_end(head,30)
head = insert_end(head,40)
print_list(head)