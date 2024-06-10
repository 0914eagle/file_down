
from itertools import combinations
from collections import defaultdict

n, q = map(int, input().split())
operations = defaultdict(list)
for _ in range(q):
    a, b = input().split()
    operations[a].append(b)
letters = ['a', 'b', 'c', 'd', 'e', 'f']
combinations = combinations(letters, n)
count = 0
for combination in combinations:
    string = ''.join(combination)
    for _ in range(n - 1):
        flag = False
        for a, b_list in operations.items():
            if string[:2] == a:
                string = string[2:] + b_list[0]
                flag = True
                break
        if not flag:
            break
    if string == 'a':
        count += 1
print(count)

