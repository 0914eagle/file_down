
def get_maximal_influence(n, spectators):
    alice_supporters = []
    bob_supporters = []
    
    for views, influence in spectators:
        if views == "11":
            alice_supporters.append(influence)
            bob_supporters.append(influence)
        elif views == "10":
            alice_supporters.append(influence)
        elif views == "01":
            bob_supporters.append(influence)
    
    alice_supporters.sort(reverse=True)
    bob_supporters.sort(reverse=True)
    
    half_n = n // 2
    min_length = min(half_n, len(alice_supporters), len(bob_supporters))
    
    total_influence = 0
    
    for i in range(min_length):
        total_influence += alice_supporters[i]
        total_influence += bob_supporters[i]
    
    return total_influence

n = int(input())
spectators = []
for _ in range(n):
    views, influence = input().split()
    spectators.append((views, int(influence)))

result = get_maximal_influence(n, spectators)
print(result)
