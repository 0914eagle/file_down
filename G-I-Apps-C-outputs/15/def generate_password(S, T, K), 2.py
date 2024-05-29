
def generate_password(S, T, K):
    password = S
    for _ in range(K):
        new_password = ""
        for char in password:
            index = ord(char) - ord('a')
            new_password += T[index]
        password = new_password
    return password

S = input().strip()
T_first = input().strip().split()
T_second = input().strip().split()
K = int(input())
M = int(input())
positions = list(map(int, input().strip().split()))

password = generate_password(S, T_first + T_second, K)

for pos in positions:
    forgotten_letter = password[pos - 1]
    print(forgotten_letter)
