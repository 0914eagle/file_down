
from collections import defaultdict

def solve(n, c):
    tape = defaultdict(list)
    for i in range(n):
        tape[c[i]].append(i + 1)
    
    instructions = []
    for color in tape:
        left = tape[color][0]
        right = tape[color][-1]
        instructions.append((left, right, color))
    
    return instructions

n = int(input())
c = list(map(int, input().split()))
instructions = solve(n, c)

if len(instructions) != len(set(c)):
    print("IMPOSSIBLE")
else:
    print(len(instructions))
    for left, right, color in instructions:
        print(left, right, color)

