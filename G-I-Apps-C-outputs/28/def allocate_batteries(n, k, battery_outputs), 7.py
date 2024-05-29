
def allocate_batteries(n, k, battery_outputs):
    battery_outputs.sort()
    min_diff = float('inf')
    
    for i in range(0, len(battery_outputs), 2*k):
        machine_batteries = battery_outputs[i:i+2*k]
        for j in range(k):
            diff = abs(machine_batteries[j] - machine_batteries[j+k])
            if diff < min_diff:
                min_diff = diff
    
    return min_diff

# Input processing
n, k = map(int, input().split())
battery_outputs = list(map(int, input().split()))

result = allocate_batteries(n, k, battery_outputs)
print(result)
```
