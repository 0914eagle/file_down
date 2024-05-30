
def is_vowelly_word(k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for n in range(1, k+1):
        if k % n == 0:
            m = k // n
            if n >= 5 and m >= 5:
                word = ''
                for i in range(n):
                    for j in range(m):
                        word += vowels[(i+j) % 5]
                return word
    
    return -1

k = int(input())
result = is_vowelly_word(k)
print(result)
