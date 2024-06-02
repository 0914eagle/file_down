
def calculate_points(rank):
    points_table = {
        1: 100, 2: 75, 3: 60, 4: 50, 5: 45, 6: 40, 7: 36, 8: 32, 9: 29, 10: 26,
        11: 24, 12: 22, 13: 20, 14: 18, 15: 16, 16: 15, 17: 14, 18: 13, 19: 12, 20: 11,
        21: 10, 22: 9, 23: 8, 24: 7, 25: 6, 26: 5, 27: 4, 28: 3, 29: 2, 30: 1
    }
    return points_table.get(rank, 0)

def calculate_aggregate_score(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sum(sorted_scores[:4])

def calculate_rank(scores, m):
    aggregate_score = calculate_aggregate_score(scores)
    better_scores = 0
    for i in range(m):
        if calculate_aggregate_score(scores[i]) > aggregate_score:
            better_scores += 1
    return 1 + better_scores

def worst_possible_rank(n, m, contestants):
    your_scores = contestants[0]
    your_rank = calculate_rank(your_scores, m)
    worst_rank = your_rank
    for i in range(1, n-1):
        temp_scores = your_scores.copy()
        temp_scores[i-1] = 0
        rank = calculate_rank(temp_scores, m)
        worst_rank = min(worst_rank, rank)
    return worst_rank

# Input parsing
n, m = map(int, input().split())
contestants = []
for _ in range(m):
    scores = list(map(int, input().split()))
    contestants.append(scores)

# Calculate and output worst possible rank
print(worst_possible_rank(n, m, contestants))
