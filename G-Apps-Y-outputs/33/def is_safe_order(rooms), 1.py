
from itertools import permutations

def is_safe_order(rooms):
    n = len(rooms)
    total_students = sum(rooms)
    total_exams = sum([rooms[i]*(n-i) for i in range(n)])
    
    if total_students != total_exams or any(rooms[i] >= n-i for i in range(n)):
        return False
    return True

def find_safe_order(n, rooms):
    for perm in permutations(range(1, n+1)):
        if is_safe_order([rooms[i] for i in perm]):
            return perm
    return "impossible"

# Input
n = int(input())
rooms = list(map(int, input().split()))

# Output
safe_order = find_safe_order(n, rooms)
if safe_order == "impossible":
    print("impossible")
else:
    print(" ".join(map(str, safe_order)))
