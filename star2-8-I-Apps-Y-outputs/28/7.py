
import sys
def input():
    return sys.stdin.readline().strip()
def main():
    S, C, K = map(int, input().split())
    socks = sorted(list(map(int, input().split())))
    machines = 0
    i = 0
    while i < len(socks):
        machines += 1
        j = i
        while j < len(socks) and socks[j] - socks[i] <= K:
            j += 1
        i = j + C - 1
    print(machines)
if __name__ == '__main__':
    main()

