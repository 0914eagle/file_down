
n = int(input())
c = [int(x) for x in input().split()]

def solve(c):
    tape = []
    for i in range(n):
        tape[c[i]] = i
    for i in range(1, n+1):
        if tape[i] != i-1:
            return "IMPOSSIBLE"
    return tape

print(solve(c))

