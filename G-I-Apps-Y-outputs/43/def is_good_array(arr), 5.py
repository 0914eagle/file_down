
def is_good_array(arr):
    total_sum = sum(arr)
    for i in range(len(arr)):
        if total_sum - arr[i] == arr[i]:
            return True
    return False

n = int(input())
array = list(map(int, input().split()))

nice_indices = []
for i in range(n):
    if is_good_array(array[:i] + array[i+1:]):
        nice_indices.append(i+1)

print(len(nice_indices))
if len(nice_indices) > 0:
    print(' '.join(map(str, nice_indices)))
``` 
