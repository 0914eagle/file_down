
def reconstruct_lineup(n, people_between):
    lineup = [1] + [0]*n
    for i in range(n-1):
        lineup[i+1] = lineup[i] + people_between[i] + 1
    return lineup

# Input
n = int(input())
people_between = list(map(int, input().split()))

# Output
order = reconstruct_lineup(n, people_between)
print(' '.join(map(str, order)))
