
def is_palindrome(s):
    return s == s[::-1]

def rearrange_palindromes(n, s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    odd_count = 0
    odd_char = ''
    for char, count in freq.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char

    if odd_count > 1:
        return -1, []

    palindromes = []
    for char, count in freq.items():
        if count % 2 == 0:
            palindromes.append(char * (count // 2))

    palindrome_length = len(palindromes[0])
    if odd_count == 1:
        palindromes.append(odd_char * (freq[odd_char] // 2))

    return palindrome_length, palindromes

n = int(input())
s = input()

length, palindromes = rearrange_palindromes(n, s)
if length == -1:
    print("Cannot rearrange into palindromes")
else:
    print(len(palindromes))
    print(" ".join(p + p[::-1] for p in palindromes))
