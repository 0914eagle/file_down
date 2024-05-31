
def find_smallest_t(n, crush):
    def find_path_length(start, crush, visited):
        if visited[start]:
            return 0
        visited[start] = True
        return 1 + find_path_length(crush[start] - 1, crush, visited)
    
    result = -1
    for i in range(n):
        visited = [False] * n
        length = find_path_length(i, crush, visited)
        if length > 0 and visited[i]:
            if result == -1:
                result = length
            else:
                result = max(result, length)
    
    return result

# Reading input
n = int(input())
crush = list(map(int, input().split()))

# Calling the function and printing the result
print(find_smallest_t(n, crush))
