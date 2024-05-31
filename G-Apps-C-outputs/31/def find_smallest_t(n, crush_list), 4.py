
def find_smallest_t(n, crush_list):
    for t in range(1, n + 1):
        visited = [False] * n
        for i in range(n):
            x = i
            for _ in range(t):
                x = crush_list[x] - 1
            if x != i:
                break
            visited[i] = True
        if all(visited):
            return t
    return -1

# Input
n = int(input())
crush_list = list(map(int, input().split()))

# Output
print(find_smallest_t(n, crush_list))
