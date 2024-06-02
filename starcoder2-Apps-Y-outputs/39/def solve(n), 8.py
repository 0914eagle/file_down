
def solve(n):
    ans = 0
    for i in range(1, n + 1):
        x = i
        cnt = 0
        while x % 2 == 0:
            cnt += 1
            x //= 2
        if cnt > ans:
            ans = cnt
            res = i
    return res

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

