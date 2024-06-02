
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

def calculate_rank(scores, on_site):
    total_points = 0
    for i, score in enumerate(scores):
        if on_site:
            score += 1
        total_points += calculate_points(i+1) * score
    return total_points

def worst_possible_rank(n, m, contestants):
    your_scores = contestants[0]
    your_aggregate_score = calculate_aggregate_score(your_scores)
    your_rank = calculate_rank(your_scores, True)
    
    other_contestants = contestants[1:]
    other_ranks = [calculate_rank(scores, False) for scores in other_contestants]
    
    better_ranks = sum(rank > your_rank for rank in other_ranks)
    potential_better_ranks = better_ranks + 1
    
    remaining_spots = 15 - potential_better_ranks
    worst_rank = potential_better_ranks + remaining_spots
    
    return worst_rank

# Input parsing
n, m = map(int, input().split())
contestants = []
for _ in range(m):
    scores = list(map(int, input().split()))
    contestants.append(scores)

result = worst_possible_rank(n, m, contestants)
print(result)
