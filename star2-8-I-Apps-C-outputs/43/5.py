
n = int(input())
s = input()

def solve(s):
    l = 0 # longest alternating subsequence
    c = 0 # current alternating subsequence
    p = -1 # previous character
    
    for ch in s:
        if ch != p:
            l = max(l, c)
            c = 1
        else:
            c += 1
        
        p = ch
    
    return max(l, c)
    
print(solve(s))

