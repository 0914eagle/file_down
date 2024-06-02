
def frog_jump_sum(m, a, b):
    def f(x):
        if x == 0:
            return 1
        reachable = set()
        reachable.add(0)
        for i in range(1, x + 1):
            if i - a in reachable or i - b in reachable:
                reachable.add(i)
        return len(reachable)

    total_sum = 0
    for i in range(m + 1):
        total_sum += f(i)
    
    return total_sum

# Input
m, a, b = map(int, input().split())

# Output
print(frog_jump_sum(m, a, b))
