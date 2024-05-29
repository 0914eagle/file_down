
def find_forgotten_letters(S, T_first, T_second, K, M, positions):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Create dictionary mappings for T_first and T_second
    first_map = {alphabet[i]: T_first[i] for i in range(13)}
    second_map = {alphabet[i]: T_second[i] for i in range(13)}
    
    def f(string, mapping):
        return ''.join([mapping[char] for char in string])
    
    password = S
    for _ in range(K):
        password = f(password, first_map)
    
    forgotten_letters = []
    for pos in positions:
        forgotten_letters.append(password[pos - 1])
    
    return forgotten_letters

# Input parsing
S = input().strip()
T_first = input().strip().split()
T_second = input().strip().split()
K = int(input())
M = int(input())
positions = list(map(int, input().strip().split()))

forgotten_letters = find_forgotten_letters(S, T_first, T_second, K, M, positions)

for letter in forgotten_letters:
    print(letter)
