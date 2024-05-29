
def generate_password(S, Ta, Tb, K):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {char: Tb[i] for i, char in enumerate(alphabet[13:])}
    mapping.update({char: Ta[i] for i, char in enumerate(alphabet[:13])})

    password = S
    for _ in range(K):
        password = ''.join([mapping[char] for char in password])

    return password

def find_forgotten_letters(S, Ta, Tb, K, M, forgotten_positions):
    password = generate_password(S, Ta, Tb, K)

    forgotten_letters = []
    for pos in forgotten_positions:
        forgotten_letters.append(password[pos - 1])

    return forgotten_letters

# Input parsing
S = input()
Ta = input().split()
Tb = input().split()
K = int(input())
M = int(input())
forgotten_positions = list(map(int, input().split()))

# Find forgotten letters
forgotten_letters = find_forgotten_letters(S, Ta, Tb, K, M, forgotten_positions)

# Output
for letter in forgotten_letters:
    print(letter)
```

