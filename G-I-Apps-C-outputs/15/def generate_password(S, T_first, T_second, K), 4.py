
def generate_password(S, T_first, T_second, K):
    password = S
    for _ in range(K):
        new_password = ''
        for char in password:
            idx = ord(char) - ord('a')
            new_password += T_first[idx]
            new_password += T_second[idx]
        password = new_password
    return password

def find_forgotten_letters(S, T_first, T_second, K, M, positions):
    password = generate_password(S, T_first, T_second, K)
    result = []
    for pos in positions:
        result.append(password[pos - 1])
    return result

# Input parsing
S = input().strip()
T_first = input().strip().split()
T_second = input().strip().split()
K = int(input())
M = int(input())
positions = list(map(int, input().strip().split()))

# Find forgotten letters
forgotten_letters = find_forgotten_letters(S, T_first, T_second, K, M, positions)

# Output forgotten letters
for letter in forgotten_letters:
    print(letter)
```
