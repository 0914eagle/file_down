
def fair_share_pie(N, slices):
    alice_pie = 0
    bob_pie = 0
    decider = "Bob"

    for slice in slices:
        if decider == "Bob":
            bob_pie += slice
            decider = "Alice"
        else:
            alice_pie += slice
            decider = "Bob"

    return alice_pie, bob_pie

# Input
N = int(input())
slices = list(map(int, input().split()))

# Output
alice_pie, bob_pie = fair_share_pie(N, slices)
print(alice_pie, bob_pie)
