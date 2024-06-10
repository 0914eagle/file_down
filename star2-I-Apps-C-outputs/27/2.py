
def find_closest_pair(arr, x):
    n = len(arr)
    diff = [abs(arr[i] - x) for i in range(n)]
    min_diff = min(diff)
    min_idx = diff.index(min_diff)
    return min_idx, min_diff

def guessing_circle(arr):
    n = len(arr)
    unique_nums = set(arr)
    for num in unique_nums:
        idx, _ = find_closest_pair(arr, num)
        if arr[(idx + 1) % n] != num and arr[(idx - 1) % n] != num:
            return num
    return "none"

n = int(input())
arr = list(map(int, input().split()))
print(guessing_circle(arr))

