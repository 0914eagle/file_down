
H, W = map(int, input().split())
a = [input() for _ in range(H)]

print("#" * (W + 2))
for s in a:
    print("#" + s + "#")
print("#" * (W + 2))

