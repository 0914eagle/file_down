
def alice_minus_bob(n, a):
    # Write your code here
    alice_score = 0
    bob_score = 0
    for i in range(0, n, 2):
        alice_score += a[i]
    for i in range(1, n, 2):
        bob_score += a[i]
    return alice_score - bob_score

n = int(input())
a = list(map(int, input().split()))
print(alice_minus_bob(n, a))

