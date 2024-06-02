
def get_prob(a, b):
    n = b - a + 1
    return (n * (n + 1) * (2 * n + 1)) / 6

def get_prob_win(a1, b1, a2, b2):
    p1 = get_prob(a1, b1)
    p2 = get_prob(a2, b2)
    return p1 / (p1 + p2)

a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())

p1 = get_prob_win(a1, b1, a3, b3)
p2 = get_prob_win(a2, b2, a4, b4)

if p1 > p2:
    print("Gunnar")
elif p1 < p2:
    print("Emma")
else:
    print("Tie")

