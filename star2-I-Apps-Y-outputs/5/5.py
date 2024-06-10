
n = int(input())
x = list(map(int, input().split()))
x.sort()

def is_power_of_two(n):
    return n != 0 and (n & (n - 1)) == 0

def find_max_subset(x):
    max_subset = 1
    max_index = 0
    for i in range(1, len(x)):
        if is_power_of_two(x[i] - x[i - 1]):
            max_subset += 1
            max_index = i
        else:
            max_subset = 1
            max_index = i
    return max_subset, max_index

max_subset, max_index = find_max_subset(x)

for i in range(max_index - max_subset + 1, max_index + 1):
    print(x[i], end=' ')
print()

