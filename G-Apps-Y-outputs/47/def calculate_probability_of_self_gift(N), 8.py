
def calculate_probability_of_self_gift(N):
    if N == 1:
        return 0.0
    elif N == 2:
        return 0.5
    else:
        return 1 - 1/2 - 1/6 + 1/24 - 1/120 + 1/720 - 1/5040 + 1/40320 - 1/362880 + 1/3628800

N = int(input())
result = calculate_probability_of_self_gift(N)
print("{:.8f}".format(result))
