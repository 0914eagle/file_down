
def solve_cave_system(A, H, n, m, passages):
    max_health = H
    for _ in range(n):
        max_health = max(max_health, H)
        for i in range(m):
            e, b, a, h = passages[i]
            if e == _ + 1:
                while H > 0 and h > 0:
                    H -= a
                    h -= A
                if H <= 0:
                    return "Oh no"
    return max_health

# Input parsing
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
print(solve_cave_system(A, H, n, m, passages))
```
