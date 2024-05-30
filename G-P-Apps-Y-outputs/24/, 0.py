
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

# Testing the function with the provided examples
head1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(hasCycle(head1))  # Output: True

head2 = ListNode(1)
node2 = ListNode(2)

head2.next = node2
node2.next = head2

print(hasCycle(head2))  # Output: True

head3 = ListNode(1)

print(hasCycle(head3))  # Output: False
```
