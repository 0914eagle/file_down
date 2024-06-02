
def fair_share_pie(N, slices):
    alice_pie = 0
    bob_pie = 0

    for i in range(N):
        if i % 2 == 0:
            if slices[0] > slices[-1]:
                alice_pie += slices[0]
                slices.pop(0)
            else:
                alice_pie += slices[-1]
                slices.pop()
        else:
            if slices[0] > slices[-1]:
                bob_pie += slices[0]
                slices.pop(0)
            else:
                bob_pie += slices[-1]
                slices.pop()

    return alice_pie, bob_pie

# Input
N = int(input())
slices = list(map(int, input().split()))

# Output
alice_pie, bob_pie = fair_share_pie(N, slices)
print(alice_pie, bob_pie)
