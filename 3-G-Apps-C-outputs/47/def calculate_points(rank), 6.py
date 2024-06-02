
def calculate_points(rank):
    if rank <= 1:
        return 100
    elif rank <= 2:
        return 75
    elif rank <= 3:
        return 60
    elif rank <= 4:
        return 50
    elif rank <= 5:
        return 45
    elif rank <= 6:
        return 40
    elif rank <= 7:
        return 36
    elif rank <= 8:
        return 32
    elif rank <= 9:
        return 29
    elif rank <= 10:
        return 26
    elif rank <= 11:
        return 24
    elif rank <= 12:
        return 22
    elif rank <= 13:
        return 20
    elif rank <= 14:
        return 18
    elif rank <= 15:
        return 16
    elif rank <= 16:
        return 15
    elif rank <= 17:
        return 14
    elif rank <= 18:
        return 13
    elif rank <= 19:
        return 12
    elif rank <= 20:
        return 11
    elif rank <= 21:
        return 10
    elif rank <= 22:
        return 9
    elif rank <= 23:
        return 8
    elif rank <= 24:
        return 7
    elif rank <= 25:
        return 6
    elif rank <= 26:
        return 5
    elif rank <= 27:
        return 4
    elif rank <= 28:
        return 3
    elif rank <= 29:
        return 2
    else:
        return 1

def calculate_aggregate_score(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sum(sorted_scores[:4])

def calculate_rank(aggregate_score, all_scores):
    ranks = [calculate_points(i) for i in range(1, 31)]
    rank = 1 + sum(1 for score in all_scores if score > aggregate_score)
    return rank

def worst_possible_rank(n, m, contestant_scores):
    your_scores = contestant_scores[0]
    all_scores = [calculate_aggregate_score(scores) for scores in contestant_scores]
    your_aggregate_score = calculate_aggregate_score(your_scores)
    your_rank = calculate_rank(your_aggregate_score, all_scores)

    if your_rank <= 15:
        return your_rank
    else:
        return min(all_scores)

# Input parsing
n, m = map(int, input().split())
contestant_scores = [list(map(int, input().split())) for _ in range(m)]

# Calculate worst possible rank
result = worst_possible_rank(n, m, contestant_scores)
print(result)
