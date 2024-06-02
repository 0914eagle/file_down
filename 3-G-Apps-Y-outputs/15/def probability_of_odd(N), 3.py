
def probability_of_odd(N):
    total_numbers = N
    odd_numbers = (N + 1) // 2
    probability = odd_numbers / total_numbers
    return probability

N = int(input())
result = probability_of_odd(N)
print("{:.10f}".format(result))
