
def refill_fridge(n, m, s, d, current_bottles):
    total_bottles = sum(current_bottles)
    max_prob = 0
    refill_scheme = []
    
    for i in range(s+1):
        new_bottles = [0] * s
        new_bottles[0] = i
        new_bottles[1] = n - i
        
        prob = 1
        for j in range(s):
            if current_bottles[j] + new_bottles[j] >= m:
                prob *= (current_bottles[j] + new_bottles[j] - m) / (current_bottles[j] + new_bottles[j])
            else:
                prob = 0
                break
        
        if prob > max_prob:
            max_prob = prob
            refill_scheme = new_bottles[:]
    
    if max_prob == 0:
        print("impossible")
    else:
        print(*refill_scheme)

# Input parsing
n, m, s, d = map(int, input().split())
current_bottles = list(map(int, input().split()))

refill_fridge(n, m, s, d, current_bottles)
