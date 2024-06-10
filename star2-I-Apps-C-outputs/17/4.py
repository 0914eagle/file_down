
def solve(num):
    num = str(num)
    n = len(num)
    if n == 1:
        return 0
    
    if n % 2 == 0:
        left = num[:n//2]
        right = num[n//2:]
    else:
        left = num[:n//2]
        right = num[n//2+1:]
    
    left = left[::-1]
    
    count = 0
    
    for i in range(len(left)):
        if left[i] != right[i]:
            count += 1
    
    return count

