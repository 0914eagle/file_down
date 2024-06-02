
def bird_lovers_club(N, correct_answers):
    adrian_sequence = 'ABC' * (N // 3) + 'ABC'[:N % 3]
    bruno_sequence = 'BABCBABCBABC' * (N // 12) + 'BABCBABCBABC'[:N % 12]
    goran_sequence = 'CCAABBCCAABB' * (N // 12) + 'CCAABBCCAABB'[:N % 12]

    adrian_score = sum(1 for i in range(N) if correct_answers[i] == adrian_sequence[i])
    bruno_score = sum(1 for i in range(N) if correct_answers[i] == bruno_sequence[i])
    goran_score = sum(1 for i in range(N) if correct_answers[i] == goran_sequence[i])

    max_score = max(adrian_score, bruno_score, goran_score)
    boys = []
    if adrian_score == max_score:
        boys.append('Adrian')
    if bruno_score == max_score:
        boys.append('Bruno')
    if goran_score == max_score:
        boys.append('Goran')

    return max_score, boys

# Input
N = int(input())
correct_answers = input().strip()

# Output
max_score, boys = bird_lovers_club(N, correct_answers)
print(max_score)
for boy in boys:
    print(boy)
