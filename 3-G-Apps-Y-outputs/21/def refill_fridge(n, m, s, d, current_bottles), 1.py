
def refill_fridge(n, m, s, d, current_bottles):
    total_capacity = s * d
    total_bottles = sum(current_bottles)
    remaining_capacity = total_capacity - total_bottles
    
    if remaining_capacity < n:
        print("impossible")
        return
    
    refill_scheme = [0] * s
    for i in range(s):
        refill_scheme[i] = min(n, remaining_capacity)
        remaining_capacity -= refill_scheme[i]
        n -= refill_scheme[i]
        
        if n == 0:
            break
    
    print(*refill_scheme)

# Input parsing
n, m, s, d = map(int, input().split())
current_bottles = list(map(int, input().split()))

# Call the function with the input values
refill_fridge(n, m, s, d, current_bottles)
