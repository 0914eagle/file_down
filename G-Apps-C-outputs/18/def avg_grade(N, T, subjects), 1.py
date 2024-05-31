
def avg_grade(N, T, subjects):
    def f_i(a, b, c, t):
        return a*t**2 + b*t + c
    
    def bin_search(a, b, c):
        low, high = 0, T
        while high - low > 1e-9:
            mid = (low + high) / 2
            if f_i(a, b, c, mid) <= 100:
                low = mid
            else:
                high = mid
        return low
    
    total_grade = 0
    for a, b, c in subjects:
        time_allocated = bin_search(a, b, c)
        total_grade += f_i(a, b, c, time_allocated)
    
    return total_grade / N

# Input
N, T = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(N)]

# Output
print("{:.10f}".format(avg_grade(N, T, subjects)))
