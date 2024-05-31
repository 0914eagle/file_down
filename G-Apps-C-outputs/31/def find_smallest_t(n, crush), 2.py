
def find_smallest_t(n, crush):
    for t in range(1, n+1):
        visited = [False] * n
        for i in range(n):
            curr = i
            for _ in range(t):
                curr = crush[curr] - 1
            if curr == i:
                visited[i] = True
        if all(visited):
            return t
    return -1

# Read input
n = int(input())
crush = list(map(int, input().split()))

# Call the function and print the result
print(find_smallest_t(n, crush))
