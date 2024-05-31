
def calculate_probability_of_self_gift(N):
    if N == 1:
        return 0.0
    elif N == 2:
        return 0.5
    else:
        return 1.0 - 1.0 / N + 1.0 / N * calculate_probability_of_self_gift(N - 1)

N = int(input().strip())
probability = calculate_probability_of_self_gift(N)
print("{:.8f}".format(probability))
