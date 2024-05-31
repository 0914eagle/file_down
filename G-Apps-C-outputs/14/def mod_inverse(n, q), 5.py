
def mod_inverse(n, q):
    return pow(n, q-2, q)

def probability_of_liking_arrangement(f, w, h):
    total_arrangements = pow(2, f + w, 10**9 + 7) - 2
    
    if h == 0:
        favorable_arrangements = total_arrangements
    else:
        favorable_arrangements = pow(2, f, 10**9 + 7)
    
    probability = (favorable_arrangements * mod_inverse(total_arrangements, 10**9 + 7)) % (10**9 + 7)
    
    return probability

# Input
f, w, h = map(int, input().split())

# Output
print(probability_of_liking_arrangement(f, w, h))
