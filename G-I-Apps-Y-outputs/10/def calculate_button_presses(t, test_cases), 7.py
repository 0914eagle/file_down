
def calculate_button_presses(t, test_cases):
    for test_case in test_cases:
        n, m = test_case[0]
        s = test_case[1]
        p = test_case[2]

        freq = [0] * 26
        total_moves = n

        for i, char in enumerate(s):
            freq[ord(char) - ord('a')] += 1

        for pi in p:
            total_moves += (n - pi)
            for i in range(pi, n):
                freq[ord(s[i]) - ord('a')] += 1

        q, r = divmod(m, total_moves - n)
        for i in range(n):
            freq[ord(s[i]) - ord('a')] *= q

        for i in range(r):
            freq[ord(s[i]) - ord('a')] += 1

        print(" ".join(map(str, freq)))

# Input parsing
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    test_cases.append((n, m, s, p))

# Call the function with the input values
calculate_button_presses(t, test_cases)
