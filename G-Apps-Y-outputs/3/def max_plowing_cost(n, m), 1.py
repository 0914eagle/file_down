
def max_plowing_cost(n, m):
    return m + (n-2)*(n-1)//2

n, m = map(int, input().split())
print(max_plowing_cost(n, m))
