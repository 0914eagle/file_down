
# Read the number of commands
n = int(input())

# Iterate through each command
for _ in range(n):
    command = input().strip()
    
    # Check if the command begins with "Simon says"
    if command.startswith("Simon says"):
        print(command[len("Simon says"):])
```
