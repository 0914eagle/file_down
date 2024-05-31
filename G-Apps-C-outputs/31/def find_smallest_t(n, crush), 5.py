
def find_smallest_t(n, crush):
    for t in range(1, n+1):
        visited = [False] * n
        for i in range(n):
            current = i
            visited[current] = True
            for j in range(t):
                current = crush[current] - 1
                if visited[current]:
                    break
                visited[current] = True
            else:
                if current == i:
                    return t
    return -1

# Input
n = int(input())
crush = list(map(int, input().split()))

# Output
print(find_smallest_t(n, crush))
