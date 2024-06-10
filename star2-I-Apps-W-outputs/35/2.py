
def solve(k, a):
    assert 1 <= k <= 10**8
    assert len(a) == 7
    assert all(x in (0, 1) for x in a)
    if sum(a) == 0:
        return -1
    if k == 1:
        return min(i for i, x in enumerate(a) if x == 1) + 1
    if k == 2:
        return min(i + 7 for i, x in enumerate(a) if x == 1) + 1
    if k == 3:
        return min(i + 14 for i, x in enumerate(a) if x == 1) + 1
    if k == 4:
        return min(i + 21 for i, x in enumerate(a) if x == 1) + 1
    if k == 5:
        return min(i + 28 for i, x in enumerate(a) if x == 1) + 1
    if k == 6:
        return min(i + 35 for i, x in enumerate(a) if x == 1) + 1
    if k == 7:
        return min(i + 42 for i, x in enumerate(a) if x == 1) + 1
    return -1

