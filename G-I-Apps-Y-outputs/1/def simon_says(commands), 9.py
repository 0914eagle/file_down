
def simon_says(commands):
    for command in commands:
        if command.startswith("Simon says"):
            print(command.replace("Simon says", "", 1))

# Taking input
n = int(input())
commands = [input() for _ in range(n)]

# Calling the simon_says function
simon_says(commands)
