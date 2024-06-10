
def solve(n, a, b):
    pos = [0] * (n + 1)
    for i in range(n):
        pos[a[i]] = i
    ans = 0
    for i in range(n):
        if b[i] == 0:
            continue
        if pos[b[i]] != i:
            ans += 1
    return ans

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))

