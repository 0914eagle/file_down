
import heapq

def find_min_final_health(N, A):
    def attack(monsters):
        attacker = heapq.heappop(monsters)  # Get the healthiest alive monster as attacker
        if not monsters:
            return
        target = heapq.heappop(monsters)  # Get the weakest alive monster as target
        remaining_health = attacker - target
        if remaining_health > 0:
            heapq.heappush(monsters, remaining_health)
        attack(monsters)

    monsters = [-health for health in A]  # Use negative health for max heap
    heapq.heapify(monsters)

    attack(monsters)
    return -monsters[0]

# Read input
N = int(input())
A = list(map(int, input().split()))

# Find and print the minimum possible final health
print(find_min_final_health(N, A))
```
