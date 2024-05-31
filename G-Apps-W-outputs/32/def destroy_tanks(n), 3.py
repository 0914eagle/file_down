
def destroy_tanks(n):
    if n == 2:
        return 3, [2, 1, 2]
    else:
        bombs = [2]
        for i in range(2, n+1):
            bombs.append(i)
            bombs.append(i-1)
        return len(bombs), bombs

n = int(input())
m, bombs = destroy_tanks(n)
print(m)
print(" ".join(map(str, bombs)))
