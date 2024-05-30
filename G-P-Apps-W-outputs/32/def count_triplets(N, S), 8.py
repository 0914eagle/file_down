
def count_triplets(N, S):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j - i != k - j:
                    count += 1
    return count

# Reading input from Standard Input
N = int(input())
S = input().strip()

result = count_triplets(N, S)
print(result)
```