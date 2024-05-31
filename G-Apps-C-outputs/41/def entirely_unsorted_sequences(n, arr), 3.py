
MOD = 10**9 + 9

def entirely_unsorted_sequences(n, arr):
    sorted_count = [0] * n
    unsorted_count = [0] * n

    for i in range(n):
        for j in range(i):
            if arr[j] <= arr[i]:
                sorted_count[i] += 1
            else:
                unsorted_count[j] += 1

    result = 1
    for i in range(n):
        result *= (n - i - sorted_count[i] - unsorted_count[i])
        result %= MOD

    return result

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(entirely_unsorted_sequences(n, arr))
