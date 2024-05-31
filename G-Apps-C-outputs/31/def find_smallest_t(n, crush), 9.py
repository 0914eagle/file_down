
def find_smallest_t(n, crush):
    crush = [x - 1 for x in crush]  # Adjusting crush indices to start from 0
    t = -1

    for i in range(n):
        visited = set()
        curr = i
        count = 0

        while curr not in visited:
            visited.add(curr)
            curr = crush[curr]
            count += 1

        if curr == i:
            if t == -1:
                t = count
            else:
                t = t * count // math.gcd(t, count)

    return t

# Input parsing
n = int(input())
crush = list(map(int, input().split()))

# Output
print(find_smallest_t(n, crush))
