
def bird_lovers_club(N, correct_answers):
    adrian_sequence = "ABC" * (N // 3) + "ABC"[:N % 3]
    bruno_sequence = "BABCBABCBABC"[:N]
    goran_sequence = "CCAABBCCAABB"[:N]

    adrian_score = sum(a == b for a, b in zip(adrian_sequence, correct_answers))
    bruno_score = sum(a == b for a, b in zip(bruno_sequence, correct_answers))
    goran_score = sum(a == b for a, b in zip(goran_sequence, correct_answers))

    max_score = max(adrian_score, bruno_score, goran_score)
    winners = []
    if adrian_score == max_score:
        winners.append("Adrian")
    if bruno_score == max_score:
        winners.append("Bruno")
    if goran_score == max_score:
        winners.append("Goran")

    return max_score, winners

# Input
N = int(input())
correct_answers = input().strip()

# Output
max_score, winners = bird_lovers_club(N, correct_answers)
print(max_score)
for winner in winners:
    print(winner)
