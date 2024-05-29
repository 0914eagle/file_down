
def last_child(n, m, children):
    line = list(range(1, n+1))
    idx = 0
    while line:
        child = line.pop(0)
        if children[child - 1] > m:
            line.append(child)
            children[child - 1] -= m
        else:
            pass
    return child

# Input
n, m = map(int, input().split())
children = list(map(int, input().split()))

# Output
print(last_child(n, m, children))
