
def count_triplets(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] in arr:
                count += 1
    return count

# Input processing
N = int(input())
arr = list(map(int, input().split()))

# Call the function and print the output
print(count_triplets(arr))
