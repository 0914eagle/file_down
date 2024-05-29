
def generate_password(S, T_dict, K):
    P = ''
    for char in S:
        P += T_dict[char]
    for _ in range(K-1):
        new_P = ''
        for char in P:
            new_P += T_dict[char]
        P = new_P
    return P

def find_forgotten_letters(S, T_dict, K, M, positions):
    P = generate_password(S, T_dict, K)
    forgotten_letters = []
    for pos in positions:
        forgotten_letters.append(P[pos - 1])
    return forgotten_letters

# Read input
S = input()
T_first_half = input().split()
T_second_half = input().split()
T_dict = {}
for i in range(26):
    char = chr(ord('a') + i)
    if i < 13:
        T_dict[char] = T_first_half[i]
    else:
        T_dict[char] = T_second_half[i-13]
K = int(input())
M = int(input())
positions = list(map(int, input().split()))

# Find forgotten letters
forgotten_letters = find_forgotten_letters(S, T_dict, K, M, positions)

# Output
for letter in forgotten_letters:
    print(letter)
```
