
def study_hours_world_A(T, X):
    hours_pass_world_A = T / X
    return hours_pass_world_A

T, X = map(int, input().split())
result = study_hours_world_A(T, X)
print("{:.10f}".format(result))
