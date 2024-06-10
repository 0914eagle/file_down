
N = int(input())
children = [input().split() for _ in range(N)]
lemonade = {'pink': 0, 'blue': 10}
for child in children:
    if child[0] == 'pink':
        lemonade[child[1]] += lemonade['pink'] * float(child[2])
    else:
        lemonade[child[0]] -= lemonade[child[0]] * float(child[2])
print(min(lemonade['blue'], 10))

