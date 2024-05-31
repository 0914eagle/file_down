
def count_ways(N, arr):
    count = 0
    sums = {}
    for i in range(N):
        for j in range(N):
            if i != j:
                target = arr[i] + arr[j]
                if target in sums:
                    count += sums[target]
                if target not in sums:
                    sums[target] = 0
                sums[target] += 1
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Call the function and output the result
print(count_ways(N, arr))
