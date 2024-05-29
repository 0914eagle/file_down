
def maximize_total_influence(n, spectators):
    alice_supporters = []
    bob_supporters = []
    neither_supporters = []

    for i in range(n):
        political_view, influence = spectators[i]
        if political_view == "00":
            neither_supporters.append((influence, i))
        elif political_view == "10":
            alice_supporters.append((influence, i))
        elif political_view == "01":
            bob_supporters.append((influence, i))
        else:
            alice_supporters.append((influence, i))
            bob_supporters.append((influence, i))

    alice_supporters.sort(reverse=True)
    bob_supporters.sort(reverse=True)
    neither_supporters.sort(reverse=True)

    selected_spectators = alice_supporters + bob_supporters
    total_spectators = len(selected_spectators)
    alice_count = 0
    bob_count = 0
    total_influence = 0

    for influence, i in selected_spectators:
        if alice_count * 2 >= total_spectators and bob_count * 2 >= total_spectators:
            break
        if alice_count < total_spectators / 2 and bob_count < total_spectators / 2:
            total_influence += influence
            if (i in [idx for _, idx in alice_supporters]) and (i in [idx for _, idx in bob_supporters]):
                alice_count += 1
                bob_count += 1
            elif i in [idx for _, idx in alice_supporters]:
                alice_count += 1
            elif i in [idx for _, idx in bob_supporters]:
                bob_count += 1

    if alice_count * 2 >= total_spectators and bob_count * 2 >= total_spectators:
        return total_influence
    else:
        return 0

# Input parsing
n = int(input())
spectators = []
for _ in range(n):
    s, a = input().split()
    spectators.append((s, int(a)))

# Output
print(maximize_total_influence(n, spectators))
