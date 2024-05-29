
def tower_of_hanoi_cost(t, n):
    def hanoi(n, source, target, aux, cost):
        if n == 1:
            return t[source][target] + cost
        else:
            step1 = hanoi(n-1, source, aux, target, cost)
            step2 = t[source][target]
            step3 = hanoi(n-1, aux, target, source, step1 + step2)
            return step3

    return hanoi(n, 0, 2, 1, 0)

# Input processing
t = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

# Calculate and output the minimum cost
result = tower_of_hanoi_cost(t, n)
print(result)
```
