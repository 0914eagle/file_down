
def main():
    n, x, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
            if i <= j and (a[i] + x * k) // x <= a[j] // x:
                ans += 1
    print(ans)

main()
