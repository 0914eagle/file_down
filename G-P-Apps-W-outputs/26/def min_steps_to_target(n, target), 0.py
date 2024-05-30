
def min_steps_to_target(n, target):
    steps = 0
    current_sum = 0
    for i in range(n-1, -1, -1):
        if target[i] > current_sum:
            steps += target[i] - current_sum
        else:
            current_sum -= target[i] - current_sum
        current_sum = (current_sum + target[i]) % 2
    return steps

n = int(input())
target = list(map(int, input().split()))

print(min_steps_to_target(n, target))
```

