
def get_forgotten_letters(S, T_first_half, T_second_half, K, M, positions):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    T_map = dict(zip(alphabet, T_first_half + T_second_half))
    
    password = S
    for _ in range(K):
        password = ''.join([T_map[char] for char in password])
    
    result = []
    for pos in positions:
        result.append(password[pos-1])
    
    return result

# Input reading and function call
S = input().strip()
T_first_half = input().split()
T_second_half = input().split()
K = int(input())
M = int(input())
positions = list(map(int, input().split()))

output = get_forgotten_letters(S, T_first_half, T_second_half, K, M, positions)

for letter in output:
    print(letter)
```

