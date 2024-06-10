
def solve(n, requests):
    max_len = 0
    left = 0
    right = 0
    sum_requests = 0
    
    while right < n:
        sum_requests += requests[right]
        
        if sum_requests > 100 * (right - left + 1):
            sum_requests -= requests[left]
            left += 1
            
        else:
            max_len = max(max_len, right - left + 1)
            right += 1
            
    return max_len

n = int(input())
requests = list(map(int, input().split()))
print(solve(n, requests))

