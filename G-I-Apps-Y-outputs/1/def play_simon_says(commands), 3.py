
def play_simon_says(commands):
    for command in commands:
        if command.startswith("Simon says"):
            print(command[len("Simon says"):].strip())

# Get input
n = int(input())
commands = [input() for _ in range(n)]

# Play Simon Says game
play_simon_says(commands)
```
