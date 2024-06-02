
def bird_lovers_club(N, correct_answers):
    adrian_sequence = ['A', 'B', 'C'] * (N // 3) + ['A', 'B', 'C'][:N % 3]
    bruno_sequence = ['B', 'A', 'B', 'C'] * (N // 3) + ['B', 'A', 'B', 'C'][:N % 4]
    goran_sequence = ['C', 'C', 'A', 'A', 'B', 'B'] * (N // 6) + ['C', 'C', 'A', 'A', 'B', 'B'][:N % 6]

    adrian_score = sum([1 for i in range(N) if adrian_sequence[i] == correct_answers[i]])
    bruno_score = sum([1 for i in range(N) if bruno_sequence[i] == correct_answers[i]])
    goran_score = sum([1 for i in range(N) if goran_sequence[i] == correct_answers[i]])

    max_score = max(adrian_score, bruno_score, goran_score)
    winners = []
    if adrian_score == max_score:
        winners.append('Adrian')
    if bruno_score == max_score:
        winners.append('Bruno')
    if goran_score == max_score:
        winners.append('Goran')

    print(max_score)
    for winner in sorted(winners):
        print(winner)

# Input parsing
N = int(input())
correct_answers = input().strip()

bird_lovers_club(N, correct_answers)
