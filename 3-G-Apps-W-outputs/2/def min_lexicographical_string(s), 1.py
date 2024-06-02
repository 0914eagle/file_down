
def min_lexicographical_string(s):
    count_0 = s.count('0')
    count_1 = s.count('1')
    count_2 = s.count('2')

    result = '0' * count_0 + '1' * count_1 + '2' * count_2

    return result

# Read input
s = input().strip()

# Call the function and print the result
print(min_lexicographical_string(s))
