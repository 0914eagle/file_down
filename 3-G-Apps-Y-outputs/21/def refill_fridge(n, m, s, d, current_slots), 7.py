
def refill_fridge(n, m, s, d, current_slots):
    total_capacity = s * d
    total_current_bottles = sum(current_slots)
    
    if total_current_bottles + n < m:
        print("impossible")
        return
    
    refill_scheme = [0] * s
    remaining_bottles = n
    
    for i in range(s):
        if remaining_bottles == 0:
            break
        
        space_available = d - current_slots[i]
        bottles_to_add = min(space_available, remaining_bottles)
        refill_scheme[i] = bottles_to_add
        remaining_bottles -= bottles_to_add
    
    print(*refill_scheme)

# Input
n, m, s, d = map(int, input().split())
current_slots = list(map(int, input().split()))

# Call the function
refill_fridge(n, m, s, d, current_slots)
