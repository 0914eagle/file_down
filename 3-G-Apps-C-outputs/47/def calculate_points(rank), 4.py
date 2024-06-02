
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

def calculate_rank(scores, my_score):
    aggregate_scores = [calculate_aggregate_score(s) for s in scores]
    my_aggregate_score = calculate_aggregate_score(my_score)
    rank = 1 + sum(score > my_aggregate_score for score in aggregate_scores)
    return rank

def worst_possible_rank(n, m, scores):
    my_score = scores[0]
    other_scores = scores[1:]
    my_rank = calculate_rank(other_scores, my_score)
    worst_rank = min(my_rank, 15)
    return worst_rank

# Input parsing
n, m = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(m)]

# Call the function and output the result
print(worst_possible_rank(n, m, scores))
