
N = int(input())
A = list(map(int, input().split()))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(0)
current = head
for a in A:
    new_node = Node(a)
    current.next = new_node
    current = new_node
current = head.next
result = []
while current is not None:
    result.append(str(current.value))
    current = current.next
print(" ".join(result))

