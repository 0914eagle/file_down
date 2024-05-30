
def alice_minus_bob(N,a):
    # Write your code here
    alice = 0
    bob = 0
    for i in range(N):
        if i%2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    return alice - bob

