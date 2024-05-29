
def count_sets(n, m):
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            candies = i**2 + j**2
            if candies % m == 0:
                ans += 1
    return ans

n, m = map(int, input().split())
print(count_sets(n, m))
