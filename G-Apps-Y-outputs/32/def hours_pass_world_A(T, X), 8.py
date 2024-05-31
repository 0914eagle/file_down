
def hours_pass_world_A(T, X):
    return T / X

T, X = map(int, input().split())
result = hours_pass_world_A(T, X)
print('{:.10f}'.format(result))
