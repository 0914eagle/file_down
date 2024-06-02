
def fair_share_pie(N, slices):
    alice_pie = 0
    bob_pie = 0

    for i in range(N):
        if i % 2 == 0:
            if slices[i] > slices[-1]:
                alice_pie += slices[i]
            else:
                bob_pie += slices[i]
        else:
            if slices[i] > slices[-1]:
                bob_pie += slices[i]
            else:
                alice_pie += slices[i]

    return alice_pie, bob_pie

# Input
N = int(input())
slices = list(map(int, input().split()))

# Output
alice_pie, bob_pie = fair_share_pie(N, slices)
print(alice_pie, bob_pie)
