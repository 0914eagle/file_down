
def max_frogs_escape(n, d, frogs):
    def can_escape(pile, frog):
        return sum(p[1] for p in pile) < frog[1]

    frogs.sort(key=lambda x: x[2], reverse=True)

    piles = []
    escaped_frogs = 0

    for frog in frogs:
        escape = False
        for pile in piles:
            if can_escape(pile, frog):
                pile.append(frog)
                escape = True
                break
        if not escape:
            if frog[2] + frog[0] > d:
                escaped_frogs += 1
            else:
                piles.append([frog])

    return escaped_frogs


# Example input parsing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

print(max_frogs_escape(n, d, frogs))
