
def largest_committee(N, K, politicians):
    def disagrees(a, b):
        return a not in politicians[b]

    def can_be_in_committee(candidate, current_committee):
        disagree_count = sum(disagrees(candidate, member) for member in current_committee)
        return disagree_count < K

    def find_largest_committee():
        largest_committee_size = 0
        for i in range(N):
            current_committee = [i]
            for j in range(N):
                if i != j and can_be_in_committee(j, current_committee):
                    current_committee.append(j)
            largest_committee_size = max(largest_committee_size, len(current_committee))
        return largest_committee_size

    return find_largest_committee()

input_line = input().split()
N = int(input_line[0])
K = int(input_line[1])
politicians = {}

for i in range(N):
    politician_line = list(map(int, input().split()))
    politicians[i] = set(politician_line[1:])

result = largest_committee(N, K, politicians)
print(result)
```
