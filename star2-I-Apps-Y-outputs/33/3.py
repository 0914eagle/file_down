
n = int(input())

def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

reachable = set()
reachable.add(n)

while True:
    n = f(n)
    if n in reachable:
        break
    reachable.add(n)

print(len(reachable))

