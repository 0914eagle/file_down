
import sys
from collections import Counter

input = sys.stdin.readline

def solve():
    n = int(input())
    s = [input().strip() for _ in range(n)]
    
    counter = Counter(s)
    max_count = max(counter.values())
    
    for k, v in counter.items():
        if v == max_count:
            print(k)

if __name__ == '__main__':
    solve()

