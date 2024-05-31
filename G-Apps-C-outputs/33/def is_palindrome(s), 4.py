
def is_palindrome(s):
    return s == s[::-1]

def rearrange_and_cut_into_palindromes(n, s):
    if n == 1:
        return 1, s

    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    odd_count = 0
    odd_char = ''
    for key, value in frequency.items():
        if value % 2 != 0:
            odd_count += 1
            odd_char = key

    if odd_count > 1:
        return 1, s

    palindromes = []
    for key, value in frequency.items():
        if value % 2 == 0:
            palindromes.append(key * (value // 2))

    if odd_count == 1:
        mid_char = odd_char
    else:
        mid_char = ''

    palindrome_length = len(palindromes[0])
    return palindrome_length, palindromes + [mid_char] + palindromes[::-1]

n = int(input())
s = input().strip()

k, result = rearrange_and_cut_into_palindromes(n, s)
print(k)
print(' '.join(result))
