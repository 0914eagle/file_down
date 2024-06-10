
n = int(input())

def helper(length, arr):
    if length == 0:
        return 1
    if length < 0:
        return 0
    count = 0
    for i in range(len(arr)):
        count += helper(length - 1, arr)
    return count

arr = [7, 8]
print(helper(n, arr))

