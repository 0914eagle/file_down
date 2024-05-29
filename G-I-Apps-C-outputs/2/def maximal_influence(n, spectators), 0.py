
def maximal_influence(n, spectators):
    alice_supporters = []
    bob_supporters = []
    total_influence = 0
    
    for i in range(n):
        views, influence = spectators[i]
        if views == "11":
            alice_supporters.append(influence)
            bob_supporters.append(influence)
        elif views == "10":
            alice_supporters.append(influence)
        elif views == "01":
            bob_supporters.append(influence)
    
    alice_supporters.sort(reverse=True)
    bob_supporters.sort(reverse=True)
    
    min_length = min(len(alice_supporters), len(bob_supporters), n // 2)
    
    for i in range(min_length):
        total_influence += alice_supporters[i] + bob_supporters[i]
    
    return total_influence

# Input parsing
n = int(input())
spectators = []
for _ in range(n):
    views, influence = input().split()
    influence = int(influence)
    spectators.append((views, influence))

# Calculate and output the maximal influence
print(maximal_influence(n, spectators))
