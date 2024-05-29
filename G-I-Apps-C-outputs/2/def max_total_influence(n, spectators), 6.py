
def max_total_influence(n, spectators):
    supporters = {
        "00": [],
        "10": [],
        "01": [],
        "11": []
    }
    
    for s, a in spectators:
        supporters[s].append(a)
    
    supporters["00"].sort(reverse=True)
    supporters["10"].sort(reverse=True)
    supporters["01"].sort(reverse=True)
    supporters["11"].sort(reverse=True)
    
    min_supporters = n // 2 + n % 2

    if len(supporters["10"]) + len(supporters["11"]) < min_supporters or len(supporters["01"]) + len(supporters["11"]) < min_supporters:
        return 0

    total_influence = 0
    alice_supporters = 0
    bob_supporters = 0

    for i in range(min_supporters):
        if len(supporters["10"]) > 0 and len(supporters["01"]) > 0:
            if supporters["10"][0] > supporters["01"][0]:
                total_influence += supporters["10"][0]
                alice_supporters += 1
                supporters["10"].pop(0)
            else:
                total_influence += supporters["01"][0]
                bob_supporters += 1
                supporters["01"].pop(0)
        elif len(supporters["10"]) > 0:
            total_influence += supporters["10"][0]
            alice_supporters += 1
            supporters["10"].pop(0)
        elif len(supporters["01"]) > 0:
            total_influence += supporters["01"][0]
            bob_supporters += 1
            supporters["01"].pop(0)
        else:
            break

    while alice_supporters < min_supporters:
        total_influence += supporters["10"][0]
        alice_supporters += 1
        supporters["10"].pop(0)

    while bob_supporters < min_supporters:
        total_influence += supporters["01"][0]
        bob_supporters += 1
        supporters["01"].pop(0)

    return total_influence

n = int(input())
spectators = []
for _ in range(n):
    s, a = input().split()
    spectators.append((s, int(a)))

print(max_total_influence(n, spectators))
```
