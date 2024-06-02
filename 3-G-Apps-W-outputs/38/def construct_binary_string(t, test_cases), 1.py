
def construct_binary_string(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        s = test_cases[i][1]

        w = ""
        for j in range(n):
            if s[j] == s[j+n-1]:
                w += s[j]
            else:
                w += "0"  # You can choose any character here

        print(w)

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Call the function
construct_binary_string(t, test_cases)
