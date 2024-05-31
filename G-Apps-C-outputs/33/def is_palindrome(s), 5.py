
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def rearrange_to_palindromes(n, s):
    # Check if the given string is already a palindrome
    if is_palindrome(s):
        return 1, [s]

    # Count the occurrences of each character in the string
    char_count = Counter(s)

    # Find the maximum count of any character
    max_count = max(char_count.values())

    # Check if it's possible to rearrange the string into palindromes
    if max_count > n // 2:
        return 1, [s]

    # Determine the length of each palindrome part
    if n % max_count == 0:
        part_length = n // max_count
    else:
        part_length = n // max_count + 1

    palindromes = ['' for _ in range(max_count)]
    curr_palindrome = 0

    # Construct the palindromes by distributing characters
    for char, count in char_count.items():
        for _ in range(count):
            palindromes[curr_palindrome] += char
            if len(palindromes[curr_palindrome]) == part_length:
                curr_palindrome += 1

    return max_count, palindromes

# Read input
n = int(input())
s = input().strip()

# Solve the problem
num_palindromes, palindromes = rearrange_to_palindromes(n, s)

# Print output
print(num_palindromes)
print(' '.join(palindromes))

