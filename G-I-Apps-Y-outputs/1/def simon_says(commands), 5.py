
def simon_says(commands):
    for command in commands:
        if command.startswith("Simon says"):
            print(command[len("Simon says"):])

# Input
n = int(input())
commands = [input() for _ in range(n)]

# Call the function
simon_says(commands)
