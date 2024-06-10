
def solve(s: str) -> int:
    n = len(s)
    min_time = 0
    for i in range(n):
        if s[i] == '1':
            min_time = max(min_time, i)
    
    return min_time

