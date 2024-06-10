
from sys import stdin

def main():
    N, A, B = map(int, stdin.readline().split())
    h = [int(stdin.readline()) for _ in range(N)]
    
    h.sort()
    
    ans = 0
    i = 0
    while i < N:
        if h[i] <= B:
            i += 1
            continue
        
        ans += 1
        h[i] -= A
        i += 1
    
    print(ans)

if __name__ == '__main__':
    main()

