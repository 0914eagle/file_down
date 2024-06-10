
def min_error(arr1, arr2, k1, k2):
    arr1.sort()
    arr2.sort(reverse=True)
    moves = min(k1, k2)
    for i in range(moves):
        arr1[i] += 1
        arr2[i] -= 1
    return sum((a - b) ** 2 for a, b in zip(arr1, arr2))

n, k1, k2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(min_error(arr1, arr2, k1, k2))

