
def is_palindrome(s):
    return s == s[::-1]

def minimum_palindromes(n, s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    odd_count = 0
    odd_char = ''
    for char, count in frequency.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char

    if odd_count > 1:
        return 1, [s]

    palindromes = []
    for char, count in frequency.items():
        if count % 2 == 0:
            palindromes.append(char * (count // 2))

    if odd_count == 1:
        palindromes.append(odd_char * (frequency[odd_char] // 2))

    k = len(palindromes)
    palindrome_length = len(palindromes[0])
    return k, [p + p[::-1] for p in palindromes]

# Read input
n = int(input())
s = input()

# Solve the problem
k, palindromes = minimum_palindromes(n, s)

# Print output
print(k)
for palindrome in palindromes:
    print(palindrome, end=' ')

