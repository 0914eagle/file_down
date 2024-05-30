
def min_steps_to_target_array(n, target):
    steps = 0
    diff = 0
    for i in range(n-1, -1, -1):
        diff += target[i] - diff
        steps += abs(diff)
    return steps

n = int(input())
target = list(map(int, input().split()))

print(min_steps_to_target_array(n, target))
```
