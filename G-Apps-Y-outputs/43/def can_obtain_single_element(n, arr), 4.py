
def can_obtain_single_element(n, arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = max(freq.values())
    total_elements = len(arr)

    if max_freq >= (total_elements + 1) // 2:
        return "YES"
    else:
        return "NO"

# Input processing
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = can_obtain_single_element(n, arr)
    print(result)
