
def refill_soda(n, m, s, d, current_slots):
    total_capacity = s * d
    total_current_sodas = sum(current_slots)
    
    if total_current_sodas + n <= m * d:
        return "impossible"
    
    refill_scheme = [0] * s
    remaining_new_bottles = n
    
    for i in range(s):
        space_available = d - current_slots[i]
        bottles_to_add = min(space_available, remaining_new_bottles)
        refill_scheme[i] = bottles_to_add
        remaining_new_bottles -= bottles_to_add
        
        if remaining_new_bottles == 0:
            break
    
    return refill_scheme

# Input
n, m, s, d = map(int, input().split())
current_slots = list(map(int, input().split()))

# Output
result = refill_soda(n, m, s, d, current_slots)
if result == "impossible":
    print("impossible")
else:
    print(*result)
