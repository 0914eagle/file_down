
def lineup(n, d):
    # Write your code here
    lineup = [1]
    for i in range(1, n):
        lineup.append(lineup[i-1] + d[i-1])
    return lineup

