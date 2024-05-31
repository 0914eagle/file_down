
def count_ways_to_choose_three_people(N, names):
    count = 0
    letter_counts = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    
    for name in names:
        first_letter = name[0]
        if first_letter in letter_counts and letter_counts[first_letter] < 1:
            letter_counts[first_letter] += 1
    
    num_valid_letters = sum(letter_counts.values())
    
    if num_valid_letters < 3:
        return 0
    
    if num_valid_letters == 3:
        return 1
    
    if num_valid_letters == 5:
        return 10
    
    return count

# Input
N = int(input())
names = [input() for _ in range(N)]

# Count ways to choose three people
ways = count_ways_to_choose_three_people(N, names)
print(ways)
