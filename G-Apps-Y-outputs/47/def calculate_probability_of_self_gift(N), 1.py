
def calculate_probability_of_self_gift(N):
    if N == 1:
        return 0.0
    elif N == 2:
        return 0.5
    else:
        probability = 1.0
        for i in range(2, N+1):
            probability *= (i - 1) / i
        return round(1 - probability, 8)

# Taking input
N = int(input())

# Calculating probability
probability = calculate_probability_of_self_gift(N)

print(probability)
