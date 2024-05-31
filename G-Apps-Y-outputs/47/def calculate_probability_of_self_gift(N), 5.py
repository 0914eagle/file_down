
def calculate_probability_of_self_gift(N):
    if N == 1:
        return 0.0
    elif N == 2:
        return 0.5
    else:
        probability = 1.0
        for i in range(1, N+1):
            probability *= (N-i) / N
        return 1 - probability

N = int(input().strip())
result = calculate_probability_of_self_gift(N)
print("{:.8f}".format(result))
