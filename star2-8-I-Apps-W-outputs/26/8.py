
n = int(input())
arr = [int(x) for x in input().split()]
freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
left = [0]*(n+1)
right = [0]*(n+1)
for i in range(1, n+1):
    left[i] = left[i-1]
    right[n-i+1] = right[n-i+2]
    if arr[i-1] in freq:
        left[i] += freq[arr[i-1]]
        freq[arr[i-1]] -= 1
    if arr[n-i] in freq:
        right[n-i+1] += freq[arr[n-i]]
        freq[arr[n-i]] -= 1
count = 0
for i in range(1, n+1):
    if left[i] > right[i+1]:
        count += 1
print(count)

