
def maximize_influence(n, people):
    alice = []
    bob = []
    both = []
    none = []
    
    for s, a in people:
        if s == "00":
            none.append(a)
        elif s == "10":
            alice.append(a)
        elif s == "01":
            bob.append(a)
        elif s == "11":
            both.append(a)
    
    alice.sort(reverse=True)
    bob.sort(reverse=True)
    both.sort(reverse=True)
    
    total_influence = sum(alice) + sum(bob)
    half = n // 2
    
    while len(alice) < half:
        if both:
            alice.append(both.pop(0))
        elif len(none) > 0:
            alice.append(none.pop(0))
        else:
            break
    
    while len(bob) < half:
        if both:
            bob.append(both.pop(0))
        elif len(none) > 0:
            bob.append(none.pop(0))
        else:
            break
    
    if len(alice) < half or len(bob) < half:
        return 0
    
    return total_influence + sum(alice) + sum(bob)

n = int(input())
people = [input().split() for _ in range(n)]
people = [(s, int(a)) for s, a in people]

result = maximize_influence(n, people)
print(result)
