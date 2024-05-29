
def expected_attempts(password_list):
    password_list.sort(key=lambda x: x[1], reverse=True)
    
    expected_attempts = sum([i * password[1] for i, password in enumerate(password_list, start=1)])
    
    return round(expected_attempts, 4)

# Input processing
n = int(input())
password_list = []
for _ in range(n):
    password, probability = input().split()
    password_list.append((password, float(probability)))

# Call the function with the input
result = expected_attempts(password_list)
print(result)
