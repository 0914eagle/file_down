
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# Test cases
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2

head3 = ListNode(1)

print(hasCycle(head1))  # Output: True
print(hasCycle(head2))  # Output: True
print(hasCycle(head3))  # Output: False
```
