
def probability_of_odd(N):
    total_integers = N
    odd_integers = (N + 1) // 2
    probability = odd_integers / total_integers
    return probability

N = int(input())
print("{:.10f}".format(probability_of_odd(N)))
