
for _ in range(int(input())):
    n = int(input())
    unfairness = 0
    prev = 0
    for i in range(1, n+1):
        unfairness += bin(i).count('1') - bin(prev).count('1')
        prev = i
    print(unfairness)

