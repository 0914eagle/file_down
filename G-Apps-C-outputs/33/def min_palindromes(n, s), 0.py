
def min_palindromes(n, s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    odd_char = None
    palindrome_parts = []
    
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char
    
    if odd_count > 1:
        return 1, [s]
    
    if odd_count == 1:
        middle_char = odd_char
        char_count[middle_char] -= 1
    
    split_char_count = {}
    part_length = 0
    for char, count in char_count.items():
        while count > 0:
            if count >= 2:
                split_char_count[char] = count // 2
                count -= 2
                part_length += 1
            else:
                split_char_count[char] = 0
                break
    
    if odd_count == 1:
        middle_part = middle_char
        part_length += 1
    
    palindrome_parts = []
    for _ in range(part_length):
        palindrome_part = ""
        for char in split_char_count:
            if split_char_count[char] > 0:
                palindrome_part += char
                split_char_count[char] -= 1
        palindrome_parts.append(palindrome_part)
    
    if odd_count == 1:
        palindrome_parts.append(middle_part)
    
    return len(palindrome_parts), palindrome_parts

n = int(input())
s = input()
k, palindromes = min_palindromes(n, s)
print(k)
print(" ".join(palindromes))
