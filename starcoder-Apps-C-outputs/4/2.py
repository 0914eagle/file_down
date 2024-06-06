
N = int(input())

arr = []
for _ in range(2 * N):
    c, a = input().split()
    arr.append((int(a), c))

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

count = 0
for i in range(2 * N):
    if arr[i][0] != i + 1:
        for j in range(i + 1, 2 * N):
            if arr[j][0] == i + 1:
                count += j - i
                while i < j:
                    swap(arr, i, j)
                    j -= 1
                break

print(count)
