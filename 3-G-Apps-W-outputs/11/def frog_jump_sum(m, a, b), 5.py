
def frog_jump_sum(m, a, b):
    def f(x):
        if x == 0:
            return 1
        reachable = set([0])
        for i in range(1, x+1):
            reachable_new = set()
            for pos in reachable:
                if pos + a <= x:
                    reachable_new.add(pos + a)
                if pos - b >= 0:
                    reachable_new.add(pos - b)
            reachable = reachable_new
        return len(reachable)
    
    total_sum = 0
    for i in range(m+1):
        total_sum += f(i)
    
    return total_sum

# Input
m, a, b = map(int, input().split())

# Output
print(frog_jump_sum(m, a, b))
