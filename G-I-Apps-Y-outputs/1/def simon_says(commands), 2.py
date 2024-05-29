
def simon_says(commands):
    for command in commands:
        if command.startswith("Simon says"):
            print(command.replace("Simon says", "", 1))

# Read input
n = int(input())
commands = []
for _ in range(n):
    commands.append(input().strip())

# Process and output
simon_says(commands)
```
