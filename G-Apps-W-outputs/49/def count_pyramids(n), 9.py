
def count_pyramids(n):
    total_pyramids = 0
    current_height = 1
    while n >= current_height * (current_height + 1) // 2:
        n -= current_height * (current_height + 1) // 2
        total_pyramids += 1
        current_height += 1
    return total_pyramids

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_pyramids(n))
