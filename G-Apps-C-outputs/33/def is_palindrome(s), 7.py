
def is_palindrome(s):
    return s == s[::-1]

def min_palindromes(n, s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    odd_chars = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_chars += 1

    if odd_chars > 1:
        return 1, [s]

    k = 2 if odd_chars == 1 else 1
    palindromes = []
    mid_char = ""
    for char, count in char_count.items():
        if count % 2 != 0:
            mid_char = char
        num_chars = count // 2
        palindromes.extend([char] * num_chars)

    if mid_char:
        palindromes.append(mid_char)

    result = []
    for i in range(k):
        result.append("".join(palindromes))

    return k, result

n = int(input())
s = input()
k, result = min_palindromes(n, s)
print(k)
print(" ".join(result))
