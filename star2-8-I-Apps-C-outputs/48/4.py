

def solve(n, tape):
  if len(set(tape)) > n:
    return "IMPOSSIBLE"
  instructions = []
  for i in range(n):
    for j in range(i, n):
      if tape[i:j + 1] == list(range(tape[i], tape[j] + 1)):
        instructions.append([i + 1, j + 1, tape[i]])
  instructions.sort(key=lambda x: x[0])
  return len(instructions)

n = int(input())
tape = list(map(int, input().split()))
print(solve(n, tape))


