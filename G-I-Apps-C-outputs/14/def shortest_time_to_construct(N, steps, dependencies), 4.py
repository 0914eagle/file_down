
def shortest_time_to_construct(N, steps, dependencies):
    times = [0] * N
    for i in range(N):
        times[i] = steps[i]

    for i in range(N):
        for dep_step in dependencies[i][1:]:
            times[i] = max(times[i], times[dep_step - 1] + steps[i])
    
    result = max(times)
    return result

# Read input
N = int(input())
steps = list(map(int, input().split()))
dependencies = []
for _ in range(N):
    deps = list(map(int, input().split()))
    dependencies.append(deps)

# Call the function and output the result
result = shortest_time_to_construct(N, steps, dependencies)
print(result)
