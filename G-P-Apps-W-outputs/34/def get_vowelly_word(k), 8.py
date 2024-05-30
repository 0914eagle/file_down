
def get_vowelly_word(k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for n in range(1, k + 1):
        if k % n == 0:
            m = k // n
            if m >= 5:
                word = ''
                for j in range(m):
                    for i in range(n):
                        word += vowels[(i + j) % 5]
                return word
    
    return -1

# Input
k = int(input().strip())

# Output
result = get_vowelly_word(k)
print(result)
