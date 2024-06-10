
def ddos(requests):
    n = len(requests)
    max_length = 0
    left = 0
    sum_requests = 0
    
    for right in range(n):
        sum_requests += requests[right]
        
        while sum_requests > 100 * (right - left + 1):
            sum_requests -= requests[left]
            left += 1
            
        max_length = max(max_length, right - left + 1)
        
    return max_length

