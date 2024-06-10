
def vowelly(k):
    n = 1
    while n <= k:
        if k % n == 0:
            m = k // n
            if n >= 5 and m >= 5:
                return True
        n += 1
    return False

def vowelly_word(k):
    if not vowelly(k):
        return -1
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = ""
    for i in range(k):
        word += vowels[i % 5]
    return word

k = int(input())
print(vowelly_word(k))

