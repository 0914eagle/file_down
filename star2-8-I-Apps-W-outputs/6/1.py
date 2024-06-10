
n, m = list(map(int, input().split()))
word1 = list(map(int, input().split()))
word2 = list(map(int, input().split()))
erased_pos1 = [i for i in range(n) if word1[i] == 0]
erased_pos2 = [i for i in range(n) if word2[i] == 0]
possibilities = 1
for i in range(n):
    if i in erased_pos1 and i in erased_pos2:
        possibilities *= (m - 1)
    elif i in erased_pos1:
        possibilities *= (m - word2[i])
    elif i in erased_pos2:
        possibilities *= (word1[i] - 1)
    else:
        if word1[i] > word2[i]:
            break
        elif word1[i] < word2[i]:
            possibilities = 0
            break
MOD = 10**9 + 7
greatest_common_divisor = 1
for i in range(2, min(possibilities, MOD) + 1):
    if possibilities % i == 0 and MOD % i == 0:
        greatest_common_divisor = i
print((possibilities // greatest_common_divisor) * pow(greatest_common_divisor, MOD - 2, MOD) % MOD)

