
from collections import deque
import sys

def solve(n, firing, hiring):
    firing_queue = deque()
    hired = set()
    hired_ids = set()
    total = 0
    result = []
    
    for i in range(n):
        fired = firing[i]
        hired_count = hiring[i]
        
        while fired > 0 and firing_queue:
            fired -= 1
            hired.remove(firing_queue.popleft())
        
        while hired_count > 0 and total < len(hired):
            total += 1
            hired_ids.add(total)
            hired.add(total)
            hired_count -= 1
        
        result.append(next(iter(hired_ids - hired)))
    
    return total, result

def main():
    n = int(sys.stdin.readline().rstrip())
    
    firing = [0] * n
    hiring = [0] * n
    
    for i in range(n):
        firing[i], hiring[i] = map(int, sys.stdin.readline().rstrip().split())
    
    total, result = solve(n, firing, hiring)
    
    print(total)
    print(*result)

if __name__ == '__main__':
    main()


