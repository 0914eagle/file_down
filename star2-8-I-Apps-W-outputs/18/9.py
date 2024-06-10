
n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
def num_explosion(h, a, b):
    h.sort(reverse=True)
    num = 0
    for i in range(len(h)):
        num += h[i] // (a - b)
        h[i] -= h[i] // (a - b) * (a - b)
        if h[i] <= b:
            break
    return num
print(num_explosion(h, a, b))

