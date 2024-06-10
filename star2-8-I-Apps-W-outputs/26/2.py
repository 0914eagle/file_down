
def solve(a):
    n = len(a)
    freq = [0] * (max(a) + 1)
    for x in a:
        freq[x] += 1
    pref_sum = [0] * (n + 1)
    for i in range(n):
        pref_sum[i + 1] = pref_sum[i] + freq[i]
    
    count = 0
    for i in range(n):
        if freq[a[i]] > pref_sum[i]:
            count += 1
    return count

n = int(input())
a = list(map(int, input().split()))
print(solve(a))

