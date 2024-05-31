
def min_operations_to_withdraw(N):
    min_operations = [float('inf')] * (N + 1)
    min_operations[0] = 0

    for i in range(1, N + 1):
        for coin in [1, 6, 9]:
            power = 0
            while coin ** power <= i:
                min_operations[i] = min(min_operations[i], min_operations[i - coin ** power] + 1)
                power += 1

    return min_operations[N]

N = int(input())
print(min_operations_to_withdraw(N))
