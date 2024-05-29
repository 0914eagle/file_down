
def max_total_influence(n, spectators):
    alice_supporters = [s for s in spectators if s[0] in ["10", "11"]]
    bob_supporters = [s for s in spectators if s[0] in ["01", "11"]]
    
    alice_supporters.sort(key=lambda x: x[1], reverse=True)
    bob_supporters.sort(key=lambda x: x[1], reverse=True)
    
    max_influence = 0
    for i in range(min(len(alice_supporters), len(bob_supporters)) + 1):
        alice_count = i
        bob_count = i
        total_influence = sum(s[1] for s in alice_supporters[:alice_count]) + sum(s[1] for s in bob_supporters[:bob_count])
        
        if alice_count * 2 >= n and bob_count * 2 >= n:
            max_influence = max(max_influence, total_influence)
    
    return max_influence

n = int(input())
spectators = []
for _ in range(n):
    views, influence = input().split()
    spectators.append((views, int(influence)))

result = max_total_influence(n, spectators)
print(result)
```
