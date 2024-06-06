
def init():
    global n, root, chairperson, m, q, a, b, boss, size, height, id
    n = int(input())
    root = int(input())
    m, q = map(int, input().split())
    id = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    height = [0] * (n + 1)
    boss = [0] * (n + 1)
    size = [0] * (n + 1)
    chairperson = [0] * (n + 1)
    for i in range(n):
        if height[i + 1] < b[i]:
            height[i + 1] = b[i]
            boss[i + 1] = root
            size[i + 1] = 0
        else:
            index = i + 1
            while height[index] >= b[i] and boss[index] != 0:
                index = boss[index]
            if height[index] < b[i]:
                height[index] = b[i]
                boss[index] = i + 1
                size[index] = 0
            else:
                height[index] = b[i]
                size[index] += 1
            boss[i + 1] = index
    for i in range(1, n + 1):
        if size[i] == 0:
            chairperson[i] = 1
            index = i
            while boss[index] != 0:
                chairperson[boss[index]] = 1
                index = boss[index]
def query(x):
    if chairperson[x] == 1:
        print(0, 0)
    else:
        index = x
        while boss[index] != 0:
            index = boss[index]
        print(id[index - 1], size[index])
init()
for i in range(q):
    query(int(input()))
