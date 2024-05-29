
def construct_airplane_shortest_time(N, steps_time, dependencies):
    # Create a directed graph representing dependencies
    graph = {i: [] for i in range(N)}
    for i, dependency in enumerate(dependencies):
        for j in dependency[1:]:
            graph[j].append(i)

    # Calculate the time taken for each step with and without eliminating it
    time_with = [0] * N
    time_without = [0] * N
    for i in range(N):
        time_with[i] = steps_time[i] + max([time_with[j] for j in graph[i]], default=0)
        time_without[i] = max([time_with[j] for j in graph[i]], default=0)

    return time_with[-1]

# Parse input
N = int(input())
steps_time = list(map(int, input().split()))
dependencies = []
for _ in range(N):
    C, *A = map(int, input().split())
    dependencies.append(A)

# Call the function and print the result
result = construct_airplane_shortest_time(N, steps_time, dependencies)
print(result)
```
