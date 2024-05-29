
def largest_committee(N, K, disagreements):
    def can_form_committee(committee):
        for member in committee:
            count_disagreements = 0
            for other_member in committee:
                if other_member != member and other_member in disagreements[member]:
                    count_disagreements += 1
            if count_disagreements >= K:
                return False
        return True

    max_size = 0
    for i in range(1, N+1):
        for subset in combinations(range(N), i):
            if can_form_committee(subset):
                max_size = max(max_size, len(subset))
    
    return max_size

# Input parsing
N, K = map(int, input().split())
disagreements = {}
for i in range(N):
    data = list(map(int, input().split()))
    disagreements[i] = set(data[1:])

print(largest_committee(N, K, disagreements))
