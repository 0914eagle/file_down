
def last_child(n, m, a):
    queue = list(range(1, n + 1))
    candies = [0] * n

    while queue:
        child = queue.pop(0)
        candies[child - 1] += min(m, a[child - 1])
        if candies[child - 1] < a[child - 1]:
            queue.append(child)
    
    return child

# Input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(last_child(n, m, a))
