
def maximize_influence(n, spectators):
    alice_supporters = []
    bob_supporters = []
    total_influence = 0
    
    for i in range(n):
        views, influence = spectators[i]
        if views == "11":
            alice_supporters.append((influence, i))
            bob_supporters.append((influence, i))
        elif views == "10":
            alice_supporters.append((influence, i))
        elif views == "01":
            bob_supporters.append((influence, i))
    
    alice_supporters.sort(reverse=True)
    bob_supporters.sort(reverse=True)
    
    selected_indices = set()
    half = (n + 1) // 2
    
    for i in range(half):
        if i < len(alice_supporters):
            total_influence += alice_supporters[i][0]
            selected_indices.add(alice_supporters[i][1])
        if i < len(bob_supporters):
            total_influence += bob_supporters[i][0]
            selected_indices.add(bob_supporters[i][1])
    
    if len(selected_indices) < half:
        return 0
    
    return total_influence

# Input
n = int(input())
spectators = [input().split() for _ in range(n)]
spectators = [(views, int(influence)) for views, influence in spectators]

# Output
print(maximize_influence(n, spectators))
