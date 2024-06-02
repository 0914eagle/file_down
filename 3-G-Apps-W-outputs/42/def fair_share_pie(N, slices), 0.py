
def fair_share_pie(N, slices):
    alice_total = 0
    bob_total = 0

    for i in range(N):
        if i % 2 == 0:
            if slices[i] > slices[-1]:
                alice_total += slices[i]
            else:
                bob_total += slices[i]
        else:
            if slices[i] > slices[-1]:
                bob_total += slices[i]
            else:
                alice_total += slices[i]

    return alice_total, bob_total

# Input
N = int(input())
slices = list(map(int, input().split()))

# Output
alice_total, bob_total = fair_share_pie(N, slices)
print(alice_total, bob_total)
