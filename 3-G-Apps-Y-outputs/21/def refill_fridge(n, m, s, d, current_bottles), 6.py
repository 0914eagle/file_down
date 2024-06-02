
def refill_fridge(n, m, s, d, current_bottles):
    total_capacity = s * d
    total_bottles = sum(current_bottles)
    remaining_capacity = total_capacity - total_bottles

    new_bottles = [0] * s
    for i in range(s):
        if remaining_capacity >= n:
            new_bottles[i] = min(n, d - current_bottles[i])
            remaining_capacity -= new_bottles[i]
            n -= new_bottles[i]
        else:
            break

    if n > 0:
        print("impossible")
    else:
        print(" ".join(map(str, new_bottles)))

# Input parsing
n, m, s, d = map(int, input().split())
current_bottles = list(map(int, input().split()))

refill_fridge(n, m, s, d, current_bottles)
