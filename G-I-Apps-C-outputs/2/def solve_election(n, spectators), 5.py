
def solve_election(n, spectators):
    alice_supporters = []
    bob_supporters = []
    
    for i in range(n):
        view, influence = spectators[i]
        if view == "11":
            alice_supporters.append((influence, i))
            bob_supporters.append((influence, i))
        elif view == "10":
            alice_supporters.append((influence, i))
        elif view == "01":
            bob_supporters.append((influence, i))
    
    alice_supporters.sort(reverse=True)
    bob_supporters.sort(reverse=True)
    
    num_alice = len(alice_supporters)
    num_bob = len(bob_supporters)
    required_alice = (n + 1) // 2
    required_bob = (n + 1) // 2
    
    total_influence = 0
    selected_alice = 0
    selected_bob = 0
    selected_indices = set()
    
    for influence, idx in alice_supporters:
        if selected_alice < required_alice:
            total_influence += influence
            selected_alice += 1
            selected_indices.add(idx)
    
    for influence, idx in bob_supporters:
        if selected_bob < required_bob and idx not in selected_indices:
            total_influence += influence
            selected_bob += 1
    
    if selected_alice >= required_alice and selected_bob >= required_bob:
        return total_influence
    else:
        return 0

# Input processing
n = int(input())
spectators = []
for _ in range(n):
    view, influence = input().split()
    spectators.append((view, int(influence)))

# Solve election problem
result = solve_election(n, spectators)
print(result)
```
