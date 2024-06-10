
n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
if len(set(arr[:n])) == 1 or len(set(arr[n:])) == 1:
    print(-1)
else:
    print(' '.join([str(x) for x in arr]))


