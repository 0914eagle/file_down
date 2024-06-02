
def find_best_sequence(N, correct_answers):
    adrian_sequence = ['A', 'B', 'C'] * (N // 3) + ['A', 'B', 'C'][:N % 3]
    bruno_sequence = ['B', 'A', 'B', 'C'] * (N // 3) + ['B', 'A', 'B', 'C'][:N % 3]
    goran_sequence = ['C', 'C', 'A', 'A', 'B', 'B'] * (N // 6) + ['C', 'C', 'A', 'A', 'B', 'B'][:N % 6]

    adrian_score = sum(1 for i in range(N) if correct_answers[i] == adrian_sequence[i])
    bruno_score = sum(1 for i in range(N) if correct_answers[i] == bruno_sequence[i])
    goran_score = sum(1 for i in range(N) if correct_answers[i] == goran_sequence[i])

    max_score = max(adrian_score, bruno_score, goran_score)
    best_boys = []
    if adrian_score == max_score:
        best_boys.append('Adrian')
    if bruno_score == max_score:
        best_boys.append('Bruno')
    if goran_score == max_score:
        best_boys.append('Goran')

    print(max_score)
    for boy in sorted(best_boys):
        print(boy)

# Input parsing
N = int(input())
correct_answers = input().strip()

find_best_sequence(N, correct_answers)
