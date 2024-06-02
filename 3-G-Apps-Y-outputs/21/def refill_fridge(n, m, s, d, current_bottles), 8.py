
def refill_fridge(n, m, s, d, current_bottles):
    total_capacity = s * d
    total_bottles = sum(current_bottles)
    remaining_space = total_capacity - total_bottles
    
    if remaining_space < n:
        print("impossible")
        return
    
    new_bottles = [0] * s
    for i in range(s):
        if remaining_space >= n:
            new_bottles[i] = min(n, d - current_bottles[i])
            remaining_space -= new_bottles[i]
            n -= new_bottles[i]
        else:
            break
    
    if n > 0:
        print("impossible")
    else:
        print(*new_bottles)

# Input
n, m, s, d = map(int, input().split())
current_bottles = list(map(int, input().split()))

# Output
refill_fridge(n, m, s, d, current_bottles)
