
def best_before(x, a, b):
    if a <= x:
        return 'safe'
    elif a <= x + 1:
        return 'dangerous'
    else:
        return 'delicious'

print(best_before(int(input().split()[0]), int(input().split()[1]), int(input().split()[2])))

