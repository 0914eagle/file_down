
import sys
from collections import deque

class LaundryMachine(object):
def __init__(self, capacity):
self.capacity = capacity
self.laundry_queue = deque()

def __str__(self):
return str(self.laundry_queue)

def add_laundry(self, laundry):
self.laundry_queue.append(laundry)

def remove_laundry(self):
return self.laundry_queue.popleft()

def is_full(self):
return len(self.laundry_queue) == self.capacity

def is_empty(self):
return len(self.laundry_queue) == 0


def solve(num_socks, capacity, max_color_diff, color_values):
laundry_machines = []
for i in range(num_socks):
laundry_machines.append(LaundryMachine(capacity))
for i in range(num_socks):
for j in range(len(laundry_machines)):
if not laundry_machines[j].is_full():
laundry_machines[j].add_laundry(color_values[i])
break

for machine in laundry_machines:
if not machine.is_empty():
laundry_value = machine.remove_laundry()

return len(laundry_machines)

num_socks, capacity, max_color_diff = map(int, input().split())
color_values = list(map(int, input().split()))
print(solve(num_socks, capacity, max_color_diff, color_values))


