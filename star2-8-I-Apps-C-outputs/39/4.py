
def solve(arr):
    n = len(arr)
    freq = [0] * (50001)
    
    for val in arr:
        freq[val + 50000] += 1
        
    count = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            sum = arr[i] + arr[j]
            if -50000 <= sum <= 50000:
                count += freq[sum + 50000]
                
    return count
n = int(input())
arr = list(map(int, input().split()))
print(solve(arr))

