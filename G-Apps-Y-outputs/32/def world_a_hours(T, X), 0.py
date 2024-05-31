
def world_a_hours(T, X):
    return T / X

T, X = map(int, input().split())
result = world_a_hours(T, X)
print("{:.10f}".format(result))
