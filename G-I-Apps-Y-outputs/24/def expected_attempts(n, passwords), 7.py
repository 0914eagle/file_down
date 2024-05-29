
def expected_attempts(n, passwords):
    passwords.sort(key=lambda x: -x[1])  # Sort passwords by probability in descending order
    expected = 0
    for i in range(n):
        expected += (i + 1) * passwords[i][1]
    return round(expected, 4)

# Input processing
N = int(input())
passwords = []
for _ in range(N):
    pwd, prob = input().split()
    passwords.append((pwd, float(prob)))

# Calculate and output the expected number of attempts
print(expected_attempts(N, passwords))
