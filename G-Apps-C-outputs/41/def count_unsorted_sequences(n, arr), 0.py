
MOD = 10 ** 9 + 9

def count_unsorted_sequences(n, arr):
    sorted_counts = [0] * n
    unsorted_counts = [0] * n

    for i in range(n):
        for j in range(i):
            if arr[j] <= arr[i]:
                sorted_counts[i] += 1
            elif arr[j] > arr[i]:
                unsorted_counts[i] += 1

    total_unsorted = 1
    for i in range(n):
        total_unsorted *= (n - i - sorted_counts[i]) % MOD
        total_unsorted %= MOD

    return total_unsorted

# Input processing
n = int(input())
arr = list(map(int, input().split()))

result = count_unsorted_sequences(n, arr)
print(result)
