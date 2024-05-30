
def count_special_triplets(N, S):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] != S[j]:
                count += len(set([S[i], S[j]])) - 1

    return count

N = int(input())
S = input().strip()
print(count_special_triplets(N, S))
```
