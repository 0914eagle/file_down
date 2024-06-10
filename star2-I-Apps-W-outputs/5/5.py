
def ddos(n, r):
    left = 0
    right = 0
    max_len = 0
    sum = 0
    
    while right < n:
        sum += r[right]
        
        while sum > 100 * (right - left + 1):
            sum -= r[left]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        right += 1
        
    return max_len
    
n = int(input())
r = list(map(int, input().split()))
print(ddos(n, r))

