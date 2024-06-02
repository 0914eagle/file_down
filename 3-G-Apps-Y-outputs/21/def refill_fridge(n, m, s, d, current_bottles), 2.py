
def refill_fridge(n, m, s, d, current_bottles):
    total_capacity = s * d
    total_bottles = sum(current_bottles)
    remaining_capacity = total_capacity - total_bottles
    
    new_bottles = [0] * s
    for i in range(s):
        if remaining_capacity >= n:
            new_bottles[i] = n
            remaining_capacity -= n
            break
        else:
            new_bottles[i] = remaining_capacity
            n -= remaining_capacity
            remaining_capacity = 0
    
    if n > 0:
        print("impossible")
    else:
        refill_scheme = [min(m, current_bottles[i] + new_bottles[i]) for i in range(s)]
        print(" ".join(map(str, refill_scheme)))

# Input
n, m, s, d = map(int, input().split())
current_bottles = list(map(int, input().split()))

# Call the function
refill_fridge(n, m, s, d, current_bottles)
