
import itertools

def calculate_probability(cold_bottles, m):
    total_bottles = sum(cold_bottles)
    probability = 1
    for i in range(m):
        probability *= cold_bottles[i] / total_bottles
        total_bottles -= cold_bottles[i]
    return probability

def optimize_fridge(n, m, s, d, c):
    max_probability = 0
    best_refill_scheme = None

    for refill_scheme in itertools.product(range(n + 1), repeat=s):
        new_fridge = c.copy()
        for i in range(s):
            new_fridge[i] += refill_scheme[i]

        cold_bottles = [min(d, new_fridge[i]) for i in range(s)]
        probability = calculate_probability(cold_bottles, m)

        if probability > max_probability:
            max_probability = probability
            best_refill_scheme = refill_scheme

    if max_probability == 0:
        return "impossible"
    else:
        return best_refill_scheme

# Input parsing
n, m, s, d = map(int, input().split())
c = list(map(int, input().split()))

result = optimize_fridge(n, m, s, d, c)
if result == "impossible":
    print("impossible")
else:
    print(*result)
