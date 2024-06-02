
def calculate_points(rank):
    points_table = {
        1: 100, 2: 75, 3: 60, 4: 50, 5: 45, 6: 40, 7: 36, 8: 32, 9: 29, 10: 26,
        11: 24, 12: 22, 13: 20, 14: 18, 15: 16, 16: 15, 17: 14, 18: 13, 19: 12, 20: 11,
        21: 10, 22: 9, 23: 8, 24: 7, 25: 6, 26: 5, 27: 4, 28: 3, 29: 2, 30: 1
    }
    
    if rank in points_table:
        return points_table[rank]
    else:
        return 0

def calculate_aggregate_score(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sum(sorted_scores[:4])

def calculate_rank(scores, your_score):
    aggregate_scores = [calculate_aggregate_score(s) for s in scores]
    your_aggregate_score = calculate_aggregate_score(your_score)
    
    rank = 1 + sum(score > your_aggregate_score for score in aggregate_scores)
    return rank

def worst_possible_rank(n, m, scores):
    your_scores = scores[0]
    other_scores = scores[1:]
    
    your_rank = calculate_rank(other_scores, your_scores)
    
    worst_rank = min(your_rank, 15)
    return worst_rank

# Input parsing
n, m = map(int, input().split())
scores = []
for _ in range(m):
    scores.append(list(map(int, input().split())))

# Calculate and output the worst possible rank
print(worst_possible_rank(n, m, scores))
