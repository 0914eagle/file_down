
def is_palindrome(s):
    return s == s[::-1]

def rearrange_cut_palindromes(n, s):
    freq_map = {}
    for char in s:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    
    palindromes = []
    length = 0
    for char, count in freq_map.items():
        if count % 2 == 1:
            length = len(char)
            break
    
    for char, count in freq_map.items():
        if count % 2 == 0:
            palindromes.extend([char]*(count//2))
        else:
            palindromes.extend([char]*(count//2))
    
    palindromes.sort()
    
    num_palindromes = len(palindromes)
    if length > 0:
        num_palindromes += 1
        
    result = []
    for i in range(num_palindromes):
        result.append(''.join(palindromes[i::num_palindromes]))

    return num_palindromes, ' '.join(result)

# Input processing
n = int(input())
s = input()

k, palindromes = rearrange_cut_palindromes(n, s)
print(k)
print(palindromes)
