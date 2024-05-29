
def is_good(arr, index_to_ignore):
    total_sum = sum(arr)
    for i in range(len(arr)):
        if i != index_to_ignore and arr[i] == total_sum - arr[i]:
            return True
    return False

n = int(input())
arr = list(map(int, input().split()))

nice_indices = []
for i in range(n):
    if is_good(arr, i):
        nice_indices.append(i+1)

print(len(nice_indices))
if len(nice_indices) > 0:
    print(" ".join(map(str, nice_indices)))
