
def min_gold_to_spend(n, m, gold_costs, friends):
    rumor_spread = [False] * n
    total_gold = 0

    for friend_pair in friends:
        x, y = friend_pair
        if not rumor_spread[x - 1] and not rumor_spread[y - 1]:
            total_gold += min(gold_costs[x - 1], gold_costs[y - 1])

    for i in range(n):
        if not rumor_spread[i]:
            total_gold += gold_costs[i]

    return total_gold

# Read input
n, m = map(int, input().split())
gold_costs = list(map(int, input().split()))
friends = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_gold_to_spend(n, m, gold_costs, friends))
