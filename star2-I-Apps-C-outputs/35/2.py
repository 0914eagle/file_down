
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def play(a, b):
    if not a or not b:
        return 0
    if a[0] == 0:
        a.pop(0)
        a.append(b.pop(0))
        return 1 + play(a, b)
    if a[0] == b[0]:
        a.pop(0)
        b.pop(0)
        return play(a, b)
    return 1 + play(a, b)

print(play(a, b))

