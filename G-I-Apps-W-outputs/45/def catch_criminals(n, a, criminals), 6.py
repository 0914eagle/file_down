
def catch_criminals(n, a, criminals):
    count = 0
    for i in range(n):
        if criminals[i] == 1:
            dist = abs(a - i + 1)
            count += 1 if dist == 1 or (dist > 1 and criminals[a-1] + criminals[i] != 2) else 0
    return count

# Example usage
n, a = map(int, input().split())
criminals = list(map(int, input().split()))
print(catch_criminals(n, a, criminals))
