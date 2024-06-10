
def solve(s, k):
    def expand(s):
        return ''.join(str(c) * (int(c) + 1) for c in s)
    
    for _ in range(50):
        s = expand(s)
    
    return s[k - 1]

s = input()
k = int(input())
print(solve(s, k))

