
a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())

def win(a, b, c, d):
    if a == c:
        return 0
    elif a > c:
        return 1
    else:
        return 2

def prob(a, b, c, d):
    if a > c:
        return 1
    elif a < c:
        return 0
    else:
        return (b - a + 1) / (d - c + 1)

w = win(a1, b1, a2, b2)
if w == 0:
    print("Tie")
elif w == 1:
    print("Gunnar")
else:
    print("Emma")


