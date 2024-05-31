
def is_palindrome(s):
    return s == s[::-1]

def rearrange_and_cut(n, s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return -1, []

    palindromes = []
    for char, count in freq.items():
        palindromes.extend([char] * (count // 2))

    if odd_count == 1:
        middle_char = [char for char, count in freq.items() if count % 2 != 0][0]
        palindromes.append(middle_char)

    palindromes.sort()

    return len(palindromes), palindromes

# Input
n = int(input())
s = input()

# Function call
num_palindromes, palindromes = rearrange_and_cut(n, s)

# Output
print(num_palindromes)
print(' '.join(palindromes))
