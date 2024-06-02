
def frog_jump_sum(m, a, b):
    def f(x):
        if x < 0:
            return 0
        if x < a:
            return x + 1
        return f(x - a) + f(x - b)
    
    total_sum = 0
    for i in range(m + 1):
        total_sum += f(i)
    
    return total_sum

# Input
m, a, b = map(int, input().split())

# Output
print(frog_jump_sum(m, a, b))
