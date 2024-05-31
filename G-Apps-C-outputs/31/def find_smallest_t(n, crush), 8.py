
def find_smallest_t(n, crush):
    for x in range(1, n + 1):
        visited = [False] * (n + 1)
        t = 1
        curr = x
        
        while not visited[curr]:
            visited[curr] = True
            curr = crush[curr - 1]
            t += 1
            if t > n:
                return -1
        
        if curr == x:
            return t - 1
    
    return -1

# Input
n = int(input())
crush = list(map(int, input().split()))

# Output
print(find_smallest_t(n, crush))
