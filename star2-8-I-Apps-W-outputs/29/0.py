
Q = int(input())

def g(x, a, b):
    return abs(x - a) + b

def f(x, updates):
    res = 0
    for a, b in updates:
        res += g(x, a, b)
    return res

def eval_query(updates):
    best_x = None
    best_y = None
    for x in range(-10**9, 10**9 + 1):
        y = f(x, updates)
        if best_y is None or y < best_y:
            best_x = x
            best_y = y
    return best_x, best_y

updates = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        updates.append((query[1], query[2]))
    else:
        best_x, best_y = eval_query(updates)
        print(best_x, best_y)

