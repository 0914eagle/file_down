
def refill_soda(n, m, s, d, current_slots):
    total_capacity = s * d
    total_current_sodas = sum(current_slots)
    
    if total_current_sodas + n > total_capacity:
        print("impossible")
        return
    
    new_slots = [0] * s
    remaining_bottles = n
    
    for i in range(s):
        if remaining_bottles == 0:
            break
        
        space_available = d - current_slots[i]
        bottles_to_add = min(space_available, remaining_bottles)
        new_slots[i] = bottles_to_add
        remaining_bottles -= bottles_to_add
    
    if remaining_bottles > 0:
        print("impossible")
        return
    
    print(*new_slots)

# Input parsing
n, m, s, d = map(int, input().split())
current_slots = list(map(int, input().split()))

# Call the function with the input values
refill_soda(n, m, s, d, current_slots)
