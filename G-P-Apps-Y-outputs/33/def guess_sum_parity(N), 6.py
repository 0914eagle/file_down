
def guess_sum_parity(N):
    total = N * (N + 1) // 2
    if total % 2 == 0:
        return 'Even'
    elif total % 2 != 0:
        return 'Odd'
    else:
        return 'Either'

# Test the function with the given example
N = 1
print(guess_sum_parity(N))
