
def fair_share_pie(N, slices):
    alice_pie = 0
    bob_pie = 0

    for i in range(N):
        if i % 2 == 0:
            if slices[-1] > slices[0]:
                alice_pie += slices.pop()
            else:
                alice_pie += slices.pop(0)
        else:
            if slices[-1] > slices[0]:
                bob_pie += slices.pop()
            else:
                bob_pie += slices.pop(0)

    return alice_pie, bob_pie

# Input
N = int(input())
slices = list(map(int, input().split()))

# Output
alice_pie, bob_pie = fair_share_pie(N, slices)
print(alice_pie, bob_pie)
