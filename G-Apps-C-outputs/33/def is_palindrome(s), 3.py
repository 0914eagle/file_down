
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def rearrange_to_palindromes(n, s):
    freq = Counter(s)
    odd_chars = [char for char, count in freq.items() if count % 2 != 0]

    palindromes = []
    while len(odd_chars) >= 2:
        char1 = odd_chars.pop()
        char2 = odd_chars.pop()
        palindromes.append(char1 + char2)
    
    even_chars = [char for char, count in freq.items() if count % 2 == 0]
    for char in even_chars:
        palindromes.extend([char] * (freq[char] // 2))

    palindromes_length = len(palindromes[0])
    
    return palindromes_length, palindromes

n = int(input())
s = input()

min_palindrome_length, palindromes = rearrange_to_palindromes(n, s)

print(len(palindromes))
print(' '.join(palindromes))
