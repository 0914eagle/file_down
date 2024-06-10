
import sys
input = sys.stdin.readline
S, C, K = map(int, input().split())
D = sorted(map(int, input().split()))

machines = 0
current_machine = 0
for sock in D:
    if current_machine == C:
        machines += 1
        current_machine = 0
    if current_machine == 0:
        minimum_color = sock
        maximum_color = sock
    if sock - minimum_color <= K and maximum_color - sock <= K:
        current_machine += 1
    else:
        machines += 1
        current_machine = 1
        minimum_color = sock
        maximum_color = sock

if current_machine > 0:
    machines += 1

print(machines)

