
def dice(a, b):
    return sum(range(a, b + 1))

def win(a1, b1, a2, b2):
    s1 = dice(a1, b1)
    s2 = dice(a2, b2)
    if s1 > s2:
        return 'Gunnar'
    elif s1 < s2:
        return 'Emma'
    else:
        return 'Tie'

a1, b1, a2, b2 = map(int, input().split())
print(win(a1, b1, a2, b2))

