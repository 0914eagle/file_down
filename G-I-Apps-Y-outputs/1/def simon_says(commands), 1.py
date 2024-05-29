
def simon_says(commands):
    for command in commands:
        if command.startswith("Simon says"):
            print(command[len("Simon says"):])

# Read input
n = int(input())
commands = [input() for _ in range(n)]

# Process and output
simon_says(commands)
```
