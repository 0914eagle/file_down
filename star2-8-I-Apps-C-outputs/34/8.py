
N = int(input())
S = set([int(input()) for i in range(N)])
S = sorted(S)
for d in S[::-1]:
    found = False
    for a in S:
        if a >= d:
            continue
        for b in S:
            if b >= d - a:
                continue
            if d - a - b in S:
                found = True
                break
        if found:
            break
    if found:
        print(d)
        break
else:
    print("no solution")

