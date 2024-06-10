
for _ in range(int(input())):
    n = int(input())
    res = 0
    for i in range(n+1):
        curr = bin(i)[2:]
        curr = (len(bin(n)[2:]) - len(curr)) * '0' + curr
        prev = bin(i-1)[2:]
        prev = (len(bin(n)[2:]) - len(prev)) * '0' + prev
        diff = 0
        for j in range(len(curr)):
            if curr[j] != prev[j]:
                diff += 1
        res += diff
    print(res)

