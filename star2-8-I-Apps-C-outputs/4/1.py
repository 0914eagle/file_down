
for t in range(int(input())):
    n = int(input())
    people = [tuple(map(int, input().split())) for _ in range(n)]
    max_people = 0
    for a in range(10001):
        for b in range(10001 - a):
            c = 10000 - a - b
            valid = True
            for ap, bp, cp in people:
                if ap > a or bp > b or cp > c:
                    valid = False
                    break
            if valid:
                max_people = max(max_people, n)

    print(f"Case #{t+1}: {max_people}")

