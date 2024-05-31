
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_common_factors(arr):
    n = len(arr)
    common_factors = [set() for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(arr[i], arr[j]) != 1:
                common_factors[i].add(j)
                common_factors[j].add(i)
    
    total_ways = 0
    
    for i in range(n):
        visited = [False] * n
        stack = [i]
        visited[i] = True
        ways = 1
        
        while stack:
            curr = stack.pop()
            for neighbor in common_factors[curr]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
                    ways += 1
        
        total_ways = max(total_ways, ways)
    
    return total_ways % (10**9 + 7)

n = int(input())
numbers = [int(input()) for _ in range(n)]
print(count_common_factors(numbers))
