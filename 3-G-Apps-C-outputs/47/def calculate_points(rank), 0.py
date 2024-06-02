
def calculate_points(rank):
    points_table = {
        1: 100, 2: 75, 3: 60, 4: 50, 5: 45, 6: 40, 7: 36, 8: 32, 9: 29, 10: 26,
        11: 24, 12: 22, 13: 20, 14: 18, 15: 16, 16: 15, 17: 14, 18: 13, 19: 12,
        20: 11, 21: 10, 22: 9, 23: 8, 24: 7, 25: 6, 26: 5, 27: 4, 28: 3, 29: 2, 30: 1
    }
    return points_table.get(rank, 0)

def calculate_aggregate_score(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sum(sorted_scores[:4])

def calculate_rank(scores, my_score):
    my_aggregate_score = calculate_aggregate_score(scores)
    rank = 1
    for score in scores:
        if calculate_aggregate_score([score, my_score]) > my_aggregate_score:
            rank += 1
    return rank

def worst_possible_rank(n, m, contestants):
    my_scores = contestants[0]
    my_score = calculate_aggregate_score(my_scores)
    my_rank = calculate_rank([score for score in my_scores if score != 0], my_score)
    
    ranks = []
    for i in range(1, m):
        contestant_scores = contestants[i]
        contestant_score = calculate_aggregate_score(contestant_scores)
        ranks.append(calculate_rank([score for score in contestant_scores if score != 0], contestant_score))
    
    worst_rank = my_rank
    for rank in ranks:
        if rank < my_rank:
            worst_rank = max(worst_rank, rank)
    
    return worst_rank

# Input parsing
n, m = map(int, input().split())
contestants = []
for _ in range(m):
    scores = list(map(int, input().split()))
    contestants.append(scores)

# Calculate and output the worst possible rank
print(worst_possible_rank(n, m, contestants))
