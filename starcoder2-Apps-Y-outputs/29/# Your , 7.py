

def dice_prob(a, b):
    return (b - a + 1) / (b + 1)

def dice_prob_win(a, b, c, d):
    p = 0
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            if i > j:
                p += dice_prob(a, b) * dice_prob(c, d)
    return p

a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())

p1 = dice_prob_win(a1, b1, a2, b2)
p2 = dice_prob_win(a3, b3, a4, b4)

if p1 > p2:
    print("Gunnar")
elif p1 < p2:
    print("Emma")
else:
    print("Tie")


