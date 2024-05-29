
def simon_says_game(N, commands):
    for command in commands:
        if command.startswith("Simon says"):
            print(command.replace("Simon says ", ""))
      
# Input processing
N = int(input())
commands = []
for _ in range(N):
    commands.append(input())

simon_says_game(N, commands)
``` 
