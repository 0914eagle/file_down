
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    heights = [int(input()) for _ in range(N)]
    heights.sort()
    min_diff = float('inf')
    for i in range(N-K+1):
        min_diff = min(min_diff, heights[i+K-1] - heights[i])
    
    print(min_diff)

if __name__ == '__main__':
    main()

