
def generate_password(S, T_list, K):
    password = S
    for _ in range(K):
        new_password = ''
        for char in password:
            index = ord(char) - ord('a')
            new_password += T_list[index]
        password = new_password
    return password

S = input().strip()
T_list_1 = input().strip().split()
T_list_2 = input().strip().split()
K = int(input())
M = int(input())
forgotten_positions = list(map(int, input().strip().split()))

password = generate_password(S, T_list_1 + T_list_2, K)

for position in forgotten_positions:
    print(password[position - 1])
