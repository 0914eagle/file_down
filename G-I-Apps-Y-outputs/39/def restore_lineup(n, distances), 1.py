
def restore_lineup(n, distances):
    lineup = [1]
    for d in distances:
        lineup.insert(d, len(lineup) + 1)
    lineup.append(len(lineup) + 1)
    return lineup

# Read input
n = int(input())
distances = list(map(int, input().split()))

# Call the function and print the output
lineup = restore_lineup(n, distances)
print(' '.join(map(str, lineup)))
