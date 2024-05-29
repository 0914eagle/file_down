
def max_total_influence(n, spectators):
    alice_supporters = []
    bob_supporters = []
    other_supporters = []

    total_influence = 0

    for s, a in spectators:
        if s == "11":
            total_influence += a
            alice_supporters.append(a)
            bob_supporters.append(a)
        elif s == "10":
            total_influence += a
            alice_supporters.append(a)
        elif s == "01":
            total_influence += a
            bob_supporters.append(a)
        else:
            other_supporters.append(a)

    if len(alice_supporters) < n // 2 or len(bob_supporters) < n // 2:
        return 0

    alice_supporters.sort()
    bob_supporters.sort()

    result = total_influence

    for i in range(len(other_supporters)):
        if len(alice_supporters) > n // 2 and len(bob_supporters) > n // 2:
            break

        if len(alice_supporters) < n // 2:
            total_influence += other_supporters[i]
            alice_supporters.append(other_supporters[i])
        elif len(bob_supporters) < n // 2:
            total_influence += other_supporters[i]
            bob_supporters.append(other_supporters[i])

        result = max(result, total_influence)

    return result


# Input parsing
n = int(input())
spectators = []
for _ in range(n):
    s, a = input().split()
    spectators.append((s, int(a)))

# Output
print(max_total_influence(n, spectators))
