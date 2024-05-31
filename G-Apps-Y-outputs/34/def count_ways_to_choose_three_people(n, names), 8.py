
def count_ways_to_choose_three_people(n, names):
    name_dict = {}
    for name in names:
        initial = name[0]
        if initial in ['M', 'A', 'R', 'C', 'H']:
            name_dict[initial] = name_dict.get(initial, 0) + 1
    
    counts = list(name_dict.values())
    if len(counts) < 3:
        return 0
    
    total_ways = 0
    for i in range(len(counts)):
        for j in range(i+1, len(counts)):
            for k in range(j+1, len(counts)):
                total_ways += counts[i] * counts[j] * counts[k]
    
    return total_ways

# Input reading from Standard Input
n = int(input())
names = []
for _ in range(n):
    names.append(input().strip())

result = count_ways_to_choose_three_people(n, names)
print(result)
