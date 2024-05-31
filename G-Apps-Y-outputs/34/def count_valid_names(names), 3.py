
def count_valid_names(names):
    count = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    for name in names:
        first_letter = name[0]
        if first_letter in count:
            count[first_letter] += 1

    total_ways = 0
    for letter1 in count:
        count_copy = count.copy()
        count_copy[letter1] -= 1
        for letter2 in count_copy:
            count_copy2 = count_copy.copy()
            count_copy2[letter2] -= 1
            for letter3 in count_copy2:
                count_copy3 = count_copy2.copy()
                count_copy3[letter3] -= 1
                if count[letter1] >= 1 and count[letter2] >= 1 and count[letter3] >= 1:
                    total_ways += 1

    return total_ways // 6

# Read input
N = int(input())
names = [input() for _ in range(N)]

# Call the function and print the result
result = count_valid_names(names)
print(result)
