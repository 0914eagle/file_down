
def find_smallest_t(n, crush):
    crush = [c - 1 for c in crush]
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    
    visited = [False] * n
    cycles = []
    
    for i in range(n):
        if not visited[i]:
            cycle_length = 1
            j = crush[i]
            visited[i] = True
            
            while j != i:
                visited[j] = True
                j = crush[j]
                cycle_length += 1
            
            cycles.append(cycle_length)
    
    result = 1
    for cycle_length in cycles:
        result = lcm(result, cycle_length)
        if result > 1e6:
            return -1
    
    return result

# Input
n = int(input())
crush = list(map(int, input().split()))

# Output
print(find_smallest_t(n, crush))
