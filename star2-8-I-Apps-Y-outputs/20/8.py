
n = int(input())
div_count = [0] * n
for i in range(1, n+1):
    while i % 2 == 0:
        div_count[i-1] += 1
        i //= 2
max_div_count = max(div_count)
candidates = [i+1 for i, x in enumerate(div_count) if x == max_div_count]
print(candidates[0])

