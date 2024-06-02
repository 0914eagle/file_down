
def hours_pass_in_world_A(T, X):
    hours_in_world_A = T / X
    return hours_in_world_A

T, X = map(int, input().split())
result = hours_pass_in_world_A(T, X)
print("{:.10f}".format(result))
