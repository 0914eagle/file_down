
def refill_soda(n, m, s, d, current_bottles):
    total_capacity = s * d
    total_current_bottles = sum(current_bottles)
    remaining_capacity = total_capacity - total_current_bottles
    
    if n > remaining_capacity:
        print("impossible")
        return
    
    refill_scheme = [0] * s
    for i in range(s):
        refill_scheme[i] = min(n, remaining_capacity)
        n -= refill_scheme[i]
        remaining_capacity -= refill_scheme[i]
    
    print(*refill_scheme)

# Input
n, m, s, d = map(int, input().split())
current_bottles = list(map(int, input().split()))

# Call the function
refill_soda(n, m, s, d, current_bottles)
