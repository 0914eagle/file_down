
class Stack:
def __init__(self):
self.items = []

def is_empty(self):
return self.items == []

def push(self, item):
self.items.append(item)

def pop(self):
return self.items.pop()

def peak(self):
return self.items[len(self.items) - 1]

def size(self):
return len(self.items)

n = int(input())
pillars = [int(i) for i in input().split()]

stack = Stack()
stack.push(pillars[0])

damage = 0
max_damage = 0
max_damage_pillar = 0

for i in range(1, n):
if stack.is_empty() or stack.peak() >= pillars[i]:
stack.push(pillars[i])
else:
while not stack.is_empty() and stack.peak() < pillars[i]:
damage += 1
stack.pop()

if damage > max_damage:
max_damage = damage
max_damage_pillar = i - damage

if damage == max_damage:
max_damage_pillar = i - damage

damage = 0

print(max_damage, max_damage_pillar)

