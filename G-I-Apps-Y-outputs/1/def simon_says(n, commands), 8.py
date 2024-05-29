
def simon_says(n, commands):
    for command in commands:
        if command.startswith("Simon says"):
            print(command.split("Simon says", 1)[1])
            
# Read input
n = int(input())
commands = []
for _ in range(n):
    commands.append(input().strip())

# Call the function
simon_says(n, commands)
```
