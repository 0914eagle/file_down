
def is_palindrome(s):
    return s == s[::-1]

def rearrange_and_cut(n, s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    palindromes = []
    for char, count in char_count.items():
        if count % 2 == 1:
            center_char = char
            center_count = count
            continue
        half_count = count // 2
        palindromes.extend([char] * half_count)
    
    if center_count:
        center_index = len(palindromes) // 2
        palindromes.insert(center_index, center_char)
    
    palindrome_length = len(palindromes)
    
    palindromes_str = ' '.join(palindromes)
    
    return palindrome_length, palindromes_str

n = int(input())
s = input()

k, palindromes = rearrange_and_cut(n, s)
print(k)
print(palindromes)
