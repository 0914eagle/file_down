
import sys
input = sys.stdin.readline

n = int(input())

fire, hire = [], []
for _ in range(n):
    f, h = map(int, input().split())
    fire.append(f)
    hire.append(h)

class Stack:
    def __init__(self):
        self.container = []
    
    def push(self, item):
        self.container.append(item)
    
    def pop(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def top(self):
        if self.is_empty():
            return None
        return self.container[-1]

min_hr = 0
hr_id = 1
hr_stack = Stack()
fired = []
for i in range(n):
    while len(fired) < fire[i]:
        hr_stack.push(hr_id)
        fired.append(hr_id)
        min_hr = max(min_hr, hr_id)
        hr_id += 1
    
    fired = fired[-(fire[i]):]
    
    for j in range(hire[i]):
        if hr_stack.top() == fired[-(j+1)]:
            hr_stack.pop()
        else:
            hr_stack.push(fired[-(j+1)])
    
    print(hr_stack.top(), end=" ")

print()
print(min_hr)

