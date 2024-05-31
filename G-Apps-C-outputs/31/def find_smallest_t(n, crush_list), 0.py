
def find_smallest_t(n, crush_list):
    crush_list = [x - 1 for x in crush_list]  # Adjusting the crush indices to be 0-based
    for t in range(1, n + 1):
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            current = i
            visited[current] = True
            while crush_list[current] != i:
                current = crush_list[current]
                visited[current] = True
            if current != i:  # For this t, not every person leads to themselves
                break
        else:
            return t
    return -1

# Input parsing
n = int(input())
crush_list = list(map(int, input().split()))

# Output
print(find_smallest_t(n, crush_list))
