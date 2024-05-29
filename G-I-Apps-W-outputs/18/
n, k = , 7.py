
n, k = map(int, input().split())
marks = list(map(int, input().split()))

current_avg = sum(marks) / n
additional_marks = 0

while True:
    target_avg = (sum(marks) + additional_marks) / (n + additional_marks)
    if target_avg >= k - 0.5:
        break
    additional_marks += 1

print(additional_marks)
```
