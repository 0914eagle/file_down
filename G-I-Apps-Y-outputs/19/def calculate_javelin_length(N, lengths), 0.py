
def calculate_javelin_length(N, lengths):
    total_length = sum(lengths)
    final_length = total_length - (N-1)
    return final_length

# Reading input
N = int(input())
lengths = []
for _ in range(N):
    lengths.append(int(input()))

# Calculating final javelin length
result = calculate_javelin_length(N, lengths)
print(result)
