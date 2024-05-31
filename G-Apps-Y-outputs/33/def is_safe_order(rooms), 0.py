
from itertools import permutations

def is_safe_order(rooms):
    n = len(rooms)
    total_students = sum(rooms)
    
    for perm in permutations(range(n)):
        pile = []
        for room_idx in perm:
            if len(pile) < rooms[room_idx]:
                return False
            pile = pile[rooms[room_idx]:] + pile[:rooms[room_idx]]
            pile.extend([1] * rooms[room_idx])
        
        if sum(pile) == total_students:
            return perm
    
    return False

# Read input
n = int(input())
rooms = list(map(int, input().split()))

# Find a safe order or output "impossible"
safe_order = is_safe_order(rooms)
if safe_order:
    print(*[room+1 for room in safe_order])
else:
    print("impossible")
