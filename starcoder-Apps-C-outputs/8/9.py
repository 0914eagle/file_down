
def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    r = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    ans = [0 for i in range(n)]
    last = [-1 for i in range(m + 1)]
    for i in range(n):
        t, c = l[i]
        ans[i] = 1
        for j in range(m):
            if p[j] <= l[i][1] - last[j + 1] <= r[j]:
                ans[i] += 1
            else:
                break
        last[c] = l[i][1]
    print(max(ans))
main()
