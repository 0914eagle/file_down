
def study_time_in_world_a(T, X):
    return T / X

T, X = map(int, input().split())
result = study_time_in_world_a(T, X)
print("{:.10f}".format(result))
