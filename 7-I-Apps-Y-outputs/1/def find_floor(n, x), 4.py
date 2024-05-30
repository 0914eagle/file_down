
def find_floor(n, x):
    if n <= 2:
        return 1
    return (n - 2) // x + 1


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    print(find_floor(n, x))

