
import math

def calculate_points(rank):
    points_table = {
        1: 100, 2: 75, 3: 60, 4: 50, 5: 45, 6: 40, 7: 36, 8: 32, 9: 29, 10: 26,
        11: 24, 12: 22, 13: 20, 14: 18, 15: 16, 16: 15, 17: 14, 18: 13, 19: 12, 20: 11,
        21: 10, 22: 9, 23: 8, 24: 7, 25: 6, 26: 5, 27: 4, 28: 3, 29: 2, 30: 1
    }
    
    if rank in points_table:
        return points_table[rank]
    else:
        avg_points = sum(points_table[i] for i in range(1, 31)) / 30
        return math.ceil(avg_points)

def calculate_aggregate_score(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sum(sorted_scores[:4])

def calculate_rank(aggregate_score, all_aggregate_scores):
    return 1 + sum(score > aggregate_score for score in all_aggregate_scores)

def worst_possible_rank(n, m, contestant_scores):
    all_aggregate_scores = []
    for scores in contestant_scores:
        aggregate_score = calculate_aggregate_score(scores)
        all_aggregate_scores.append(aggregate_score)
    
    your_aggregate_score = all_aggregate_scores[0]
    your_rank = calculate_rank(your_aggregate_score, all_aggregate_scores)
    
    return your_rank

# Input parsing
n, m = map(int, input().split())
contestant_scores = []
for _ in range(m):
    scores = list(map(int, input().split()))
    contestant_scores.append(scores)

# Calculate and output worst possible rank
print(worst_possible_rank(n, m, contestant_scores))
