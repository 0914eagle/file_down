
N = int(input())
children = []
for _ in range(N):
    O, W, R = input().split()
    R = float(R)
    children.append((O, W, R))

children.sort(key=lambda x: x[2])

result = 0
blue_lemonade = 1
for O, W, R in children:
    if W == "pink":
        if O == "blue":
            result += blue_lemonade * R
            break
        else:
            blue_lemonade *= R
print(min(result, 10))

