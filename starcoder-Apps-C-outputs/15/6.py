
def count_confused_sequence(n, c):
    if n == 1:
        return 1 if c == 0 else 0
    elif n == 2:
        return 2 if c == 1 else 1
    elif c == 0:
        return 1
    else:
        total = 0
        for i in range(c+1):
            total += count_confused_sequence(n-1, i)
        return total

if __name__ == "__main__":
    n, c = map(int, input().split())
    print(count_confused_sequence(n, c) % 1000000007)
