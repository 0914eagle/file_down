
n = int(input())

for _ in range(n):
    command = input()
    if command.startswith("Simon says"):
        print(command[len("Simon says"):].strip())
```
