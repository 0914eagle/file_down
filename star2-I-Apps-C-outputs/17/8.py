
def solve(s):
    n = len(s)
    if n == 1:
        return 0
    
    if n % 2 == 0:
        left = s[:n//2]
        right = s[n//2:]
    else:
        left = s[:n//2]
        right = s[n//2+1:]
    
    left = left[::-1]
    
    carry = 0
    
    for i in range(len(left)):
        if left[i] != right[i]:
            diff = abs(ord(left[i]) - ord(right[i]))
            carry += diff
    
    return carry

s = input()
print(solve(s))

