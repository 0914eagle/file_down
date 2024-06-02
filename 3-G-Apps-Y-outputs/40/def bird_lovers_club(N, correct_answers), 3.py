
def bird_lovers_club(N, correct_answers):
    adrian_sequence = ['A', 'B', 'C'] * (N // 3) + ['A', 'B', 'C'][:N % 3]
    bruno_sequence = ['B', 'A', 'B', 'C'] * (N // 3) + ['B', 'A', 'B', 'C'][:N % 4]
    goran_sequence = ['C', 'C', 'A', 'A', 'B', 'B'] * (N // 6) + ['C', 'C', 'A', 'A', 'B', 'B'][:N % 6]

    adrian_score = sum(1 for i in range(N) if adrian_sequence[i] == correct_answers[i])
    bruno_score = sum(1 for i in range(N) if bruno_sequence[i] == correct_answers[i])
    goran_score = sum(1 for i in range(N) if goran_sequence[i] == correct_answers[i])

    max_score = max(adrian_score, bruno_score, goran_score)
    result = []
    if adrian_score == max_score:
        result.append('Adrian')
    if bruno_score == max_score:
        result.append('Bruno')
    if goran_score == max_score:
        result.append('Goran')

    return max_score, result

# Input
N = int(input())
correct_answers = input().strip()

# Output
max_score, result = bird_lovers_club(N, correct_answers)
print(max_score)
for boy in result:
    print(boy)
