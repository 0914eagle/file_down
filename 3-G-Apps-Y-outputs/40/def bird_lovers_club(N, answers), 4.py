
def bird_lovers_club(N, answers):
    adrian_sequence = ['A', 'B', 'C'] * (N // 3) + ['A', 'B', 'C'][:N % 3]
    bruno_sequence = ['B', 'A', 'B', 'C'] * (N // 3) + ['B', 'A', 'B', 'C'][:N % 4]
    goran_sequence = ['C', 'C', 'A', 'A', 'B', 'B'] * (N // 6) + ['C', 'C', 'A', 'A', 'B', 'B'][:N % 6]

    adrian_score = sum([1 for i in range(N) if adrian_sequence[i] == answers[i]])
    bruno_score = sum([1 for i in range(N) if bruno_sequence[i] == answers[i]])
    goran_score = sum([1 for i in range(N) if goran_sequence[i] == answers[i]])

    max_score = max(adrian_score, bruno_score, goran_score)
    result = []
    if adrian_score == max_score:
        result.append('Adrian')
    if bruno_score == max_score:
        result.append('Bruno')
    if goran_score == max_score:
        result.append('Goran')

    print(max_score)
    for name in sorted(result):
        print(name)

# Input
N = int(input())
answers = input().strip()

# Call the function
bird_lovers_club(N, answers)
