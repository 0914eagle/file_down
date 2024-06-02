
def optimal_split(n, pieces):
    pieces.sort(reverse=True)
    alice_sum = 0
    bob_sum = 0

    for i in range(n):
        if i % 2 == 0:
            alice_sum += pieces[i]
        else:
            bob_sum += pieces[i]

    return alice_sum, bob_sum

# Input
n = int(input())
pieces = list(map(int, input().split()))

# Output
alice_sum, bob_sum = optimal_split(n, pieces)
print(alice_sum, bob_sum)
