
def count_scary_subarrays(n, arr):
    count = 0
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            subarray.sort()
            median = subarray[len(subarray)//2] if len(subarray) % 2 != 0 else (subarray[len(subarray)//2 - 1] + subarray[len(subarray)//2]) / 2
            if subarray[0] == median:
                count += 1
    return count

# Input processing
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(count_scary_subarrays(n, arr))
