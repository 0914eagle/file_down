
def generate_password(S, T_list, K):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = dict(zip(alphabet, T_list))
    
    password = S
    for _ in range(K):
        new_password = ''
        for char in password:
            new_password += mapping[char]
        password = new_password

    return password

def find_forgotten_letters(S, T_list, K, M, positions):
    password = generate_password(S, T_list, K)
    
    forgotten_letters = []
    for pos in positions:
        forgotten_letters.append(password[pos-1])
    
    return forgotten_letters

# Input parsing
S = input().strip()
T_list1 = input().strip().split()
T_list2 = input().strip().split()
K = int(input())
M = int(input())
positions = list(map(int, input().strip().split()))

# Call the function to find the forgotten letters
forgotten_letters = find_forgotten_letters(S, T_list1 + T_list2, K, M, positions)

# Output the result
for letter in forgotten_letters:
    print(letter)
