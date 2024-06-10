
def solve(n, requests):
    max_length = 0
    current_length = 0
    threshold = 100 * n
    total_requests = 0
    
    for request in requests:
        total_requests += request
        
        if total_requests > threshold:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
            
    return max_length

n = int(input())
requests = list(map(int, input().split()))

print(solve(n, requests))

