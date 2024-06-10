
import sys

def solve(a, b, n, m):
    if n == 0 or m == 0:
        return "No"
    
    if a == 0 and b == 0:
        return "No"
    
    while a <= b and n > 0:
        n -= 1
        a += 1
    
    while b <= a and m > 0:
        m -= 1
        b += 1
    
    if a < b:
        return "Yes"
    
    return "No"
    
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a, b, n, m = map(int, input().split())
        
        print(solve(a, b, n, m))

