
def count_triplets(N, S):
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j - i != k - j:
                    count += 1
    return count

# Input processing
N = int(input())
S = input().strip()

# Call the function to count the triplets
result = count_triplets(N, S)

# Print the result
print(result)
```
