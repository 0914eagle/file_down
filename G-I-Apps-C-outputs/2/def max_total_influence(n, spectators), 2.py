
def max_total_influence(n, spectators):
    alice_supporters = []
    bob_supporters = []
    none_supporters = []
    both_supporters = []

    for s, a in spectators:
        if s == "10":
            alice_supporters.append(a)
        elif s == "01":
            bob_supporters.append(a)
        elif s == "00":
            none_supporters.append(a)
        else:
            both_supporters.append(a)

    alice_supporters.sort(reverse=True)
    bob_supporters.sort(reverse=True)
    none_supporters.sort(reverse=True)
    both_supporters.sort(reverse=True)

    total_influence = 0
    m = len(spectators) // 2

    if len(alice_supporters) + len(both_supporters) < m or len(bob_supporters) + len(both_supporters) < m:
        return 0

    if len(alice_supporters) >= m and len(bob_supporters) >= m:
        total_influence = sum(alice_supporters[:m]) + sum(bob_supporters[:m])
    else:
        additional_spectators = m - min(len(alice_supporters), len(bob_supporters))
        total_influence = sum(alice_supporters[:m + additional_spectators]) + sum(bob_supporters[:m + additional_spectators])

    return total_influence


n = int(input())
spectators = []
for _ in range(n):
    s, a = input().split()
    spectators.append((s, int(a)))

result = max_total_influence(n, spectators)
print(result)
