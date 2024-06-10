
N, L = map(int, input().split())
apples = [L + i - 1 for i in range(1, N + 1)]
min_abs_diff = float('inf')
for apple in apples:
    remaining_apples = [flavor for flavor in apples if flavor != apple]
    remaining_apple_pie = sum(remaining_apples)
    abs_diff = abs(sum(apples) - remaining_apple_pie)
    min_abs_diff = min(min_abs_diff, abs_diff)
print(min_abs_diff)

