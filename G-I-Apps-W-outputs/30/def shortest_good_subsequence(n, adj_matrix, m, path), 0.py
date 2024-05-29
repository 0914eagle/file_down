
from itertools import permutations

def shortest_good_subsequence(n, adj_matrix, m, path):
    shortest_length = float('inf')
    shortest_subsequence = []

    for k in range(2, m + 1):
        for subsequence in permutations(path, k):
            valid = True
            for i in range(k - 1):
                if adj_matrix[subsequence[i] - 1][subsequence[i + 1] - 1] != '1':
                    valid = False
                    break

            if valid:
                length = sum([adj_matrix[subsequence[i] - 1][subsequence[i + 1] - 1] == '1' for i in range(k - 1)])
                if length < shortest_length:
                    shortest_length = length
                    shortest_subsequence = subsequence

    return shortest_length, shortest_subsequence

# Read input
n = int(input())
adj_matrix = [input().strip() for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

# Call the function and print the output
length, subsequence = shortest_good_subsequence(n, adj_matrix, m, path)
print(length)
print(*subsequence)
