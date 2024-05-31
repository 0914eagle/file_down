
def find_smallest_t(n, crush):
    for i in range(n):
        visited = [False] * n
        j = i
        t = 1
        while not visited[j]:
            visited[j] = True
            j = crush[j] - 1
            if t > 1 and j == i:
                return t
            t += 1
    return -1

# Read input
n = int(input())
crush = list(map(int, input().split()))

# Find and print the smallest t
print(find_smallest_t(n, crush))
