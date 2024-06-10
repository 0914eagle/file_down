
S, C, K = map(int, input().split())
socks = sorted(map(int, input().split()))

current_machine = 0
washing_machine = [[] for _ in range(S)]
for sock in socks:
  if len(washing_machine[current_machine]) < C and all(abs(sock - w) <= K for w in washing_machine[current_machine]):
    washing_machine[current_machine].append(sock)
  else:
    current_machine += 1
    washing_machine[current_machine] = [sock]

print(current_machine + 1)

