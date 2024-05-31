
def calculate_probability(N):
    if N == 1:
        return 0
    prob_no_self_gift = 1
    prob_self_gift = 0

    for i in range(1, N+1):
        prob_self_gift += (prob_no_self_gift / N)
        prob_no_self_gift *= (N - i) / N

    return round(prob_self_gift, 8)

# Read input
N = int(input())

# Calculate and print the probability
print(calculate_probability(N))
