
from collections import defaultdict

N, D, C = list(map(int, input().split()))
cesar = set(map(int, input().split()))
raul = set(map(int, input().split()))

counter = defaultdict(int)

for i in range(C):
    for j in range(C):
        counter[min(cesar[i], raul[j]) + max(cesar[i], raul[j])] += 1

P = 0
for k, v in counter.items():
    P += v / (N * N)

D = D if D <= N else N

print(sum([((-1)**(D-i) * binom(D, i) * P**i * (1-P)**(D-i)) / (1 - (1-P)**D) for i in range(D+1)]))
