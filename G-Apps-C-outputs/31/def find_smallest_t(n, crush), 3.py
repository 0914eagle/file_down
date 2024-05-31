
def find_smallest_t(n, crush):
    for t in range(1, n+1):
        visited = [False] * (n+1)
        for i in range(1, n+1):
            curr = i
            steps = 0
            while not visited[curr]:
                visited[curr] = True
                steps += 1
                curr = crush[curr-1]
                if steps % t == 0 and curr == i:
                    break
            if not visited[i]:
                break
        else:
            return t
    return -1

# Input reading
n = int(input())
crush = list(map(int, input().split()))

# Call the function and print the result
print(find_smallest_t(n, crush))
