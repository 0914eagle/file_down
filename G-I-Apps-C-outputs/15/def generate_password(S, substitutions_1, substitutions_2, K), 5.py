
def generate_password(S, substitutions_1, substitutions_2, K):
    def apply_substitution(ch, substitutions):
        return substitutions[ord(ch) - ord('a')]

    def apply_function(password, substitutions):
        result = ''
        for ch in password:
            result += apply_substitution(ch, substitutions)
        return result

    password = S
    for _ in range(K):
        password = apply_function(password, substitutions_1)

    return password

def solve_forgotten_letters(S, substitutions_1, substitutions_2, K, M, positions):
    password = generate_password(S, substitutions_1, substitutions_2, K)
    forgotten_letters = [password[position - 1] for position in positions]
    return forgotten_letters

# Input
S = input().strip()
substitutions_1 = input().strip().split()
substitutions_2 = input().strip().split()
K = int(input().strip())
M = int(input().strip())
positions = list(map(int, input().strip().split()))

forgotten_letters = solve_forgotten_letters(S, substitutions_1, substitutions_2, K, M, positions)

# Output
for letter in forgotten_letters:
    print(letter)
```
