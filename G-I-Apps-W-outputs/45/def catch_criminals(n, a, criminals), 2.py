
def catch_criminals(n, a, criminals):
    caught = 0
    for i in range(n):
        if criminals[i] == 1:
            distance = abs(a - i + 1)
            if i != a:
                if criminals[i] == 1 and distance < n:
                    caught += 1
    return caught

# Example usage
n, a = map(int, input().split())
criminals = list(map(int, input().split()))
print(catch_criminals(n, a, criminals))
