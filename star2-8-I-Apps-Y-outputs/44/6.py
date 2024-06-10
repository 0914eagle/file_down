
import sys
from collections import deque

def solve():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))
    
    conversations = deque()
    
    for id in ids:
        if id in conversations:
            conversations.remove(id)
        
        conversations.appendleft(id)
        
        if len(conversations) > k:
            conversations.pop()
    
    print(len(conversations))
    print(' '.join(map(str, conversations)))

solve()


