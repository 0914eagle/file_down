
def bird_lovers_club(N, correct_answers):
    adrian_sequence = 'ABC' * (N // 3) + 'ABC'[:N % 3]
    bruno_sequence = 'BABCBABC' * (N // 8) + 'BABCBABC'[:N % 8]
    goran_sequence = 'CCAABB' * (N // 6) + 'CCAABB'[:N % 6]

    adrian_score = sum(1 for i in range(N) if correct_answers[i] == adrian_sequence[i])
    bruno_score = sum(1 for i in range(N) if correct_answers[i] == bruno_sequence[i])
    goran_score = sum(1 for i in range(N) if correct_answers[i] == goran_sequence[i])

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
