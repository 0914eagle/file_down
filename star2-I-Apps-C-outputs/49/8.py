
def dog_show(bowls, T):
    bowls = [(t, i) for i, t in enumerate(bowls)]
    bowls.sort()
    eaten = 0
    pos = 0
    for t, i in bowls:
        if t > T:
            break
        if pos < i:
            pos = i
            eaten += 1
        elif pos == i:
            eaten += 1
        T -= 1
    return eaten

n, T = map(int, input().split())
bowls = list(map(int, input().split()))
print(dog_show(bowls, T))

