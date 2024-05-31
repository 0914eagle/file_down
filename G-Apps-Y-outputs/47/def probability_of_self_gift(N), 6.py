
def probability_of_self_gift(N):
    if N == 1:
        return 0.0
    elif N == 2:
        return 0.5
    else:
        probability = 1.0
        for i in range(1, N+1):
            probability *= (N-i) / N
            if probability < 1e-6:
                break
        return round(1 - probability, 8)

# Read input
N = int(input())

# Calculate and output the probability
result = probability_of_self_gift(N)
print("{:.8f}".format(result))
