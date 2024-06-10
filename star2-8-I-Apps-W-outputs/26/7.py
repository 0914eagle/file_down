
def solution(arr):
    n = len(arr)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    freq = {}
    
    for i in range(n):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        left[i] = freq[arr[i]]
        
    freq = {}
    
    for i in range(n-1, -1, -1):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        right[i] = freq[arr[i]]
        
    count = 0
    
    for i in range(n-1):
        if left[i] > right[i+1]:
            count += 1
            
    return count

