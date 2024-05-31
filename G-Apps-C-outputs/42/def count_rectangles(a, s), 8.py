
def count_rectangles(a, s):
    n = len(s)
    b = [[int(s[i]) * int(s[j]) for j in range(n)] for i in range(n)]
    count = 0

    for x in range(n):
        for y in range(x, n):
            for z in range(n):
                for t in range(z, n):
                    total = 0
                    for i in range(x, y+1):
                        for j in range(z, t+1):
                            total += b[i][j]
                    if total == a:
                        count += 1

    return count

# Input
a = int(input())
s = input().strip()

# Output
print(count_rectangles(a, s))
