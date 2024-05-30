
def generate_vowelly_word(k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Check if k is divisible by any number from 1 to 5 to form a vowelly word
    for i in range(1, 6):
        if k % i == 0:
            n = i
            m = k // i
            if n >= 5 and m >= 5:
                vowelly_word = ''
                for j in range(n):
                    for v in vowels:
                        vowelly_word += v
                vowelly_word = vowelly_word * m
                return vowelly_word
    
    return -1

# Input
k = int(input().strip())

# Output
result = generate_vowelly_word(k)
print(result)
