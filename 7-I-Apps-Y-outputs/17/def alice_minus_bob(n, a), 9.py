
def alice_minus_bob(n, a):
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    return alice - bob

