
import sys

def solve(n, k, h):
    if n == 1:
        return k
    
    count = 0
    
    for answer in range(1, k+1):
        if h[0] == answer:
            new_h = h[1:]
        else:
            new_h = h[1:] + [answer]
        
        if sum(new_h) > sum(h):
            count += 1
    
    return count

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    
    print(solve(n, k, h))

if __name__ == "__main__":
    main()

