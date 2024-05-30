
def alice_minus_bob(n, a):
    alice_score = 0
    bob_score = 0
    for i in range(n):
        if i % 2 == 0:
            alice_score += a[i]
        else:
            bob_score += a[i]
    return alice_score - bob_score

