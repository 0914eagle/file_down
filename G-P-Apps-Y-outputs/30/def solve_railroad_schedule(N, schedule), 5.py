
def solve_railroad_schedule(N, schedule):
    times = [0] * N
    for i in range(N - 1):
        for j in range(i, N - 1):
            S_i, F_i, C_i = schedule[j]
            if times[j] <= S_i:
                times[j] = S_i
            else:
                times[j] = ((times[j] - S_i + F_i - 1) // F_i) * F_i + S_i
            times[j] += C_i
    for t in times:
        print(t)

# Sample Input Parsing
N = 3
schedule = [(6, 5, 1), (1, 10, 1)]

solve_railroad_schedule(N, schedule)
```
