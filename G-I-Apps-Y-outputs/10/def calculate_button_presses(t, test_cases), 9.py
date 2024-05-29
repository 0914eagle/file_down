
def calculate_button_presses(t, test_cases):
    for i in range(t):
        n, m = test_cases[i][0]
        s = test_cases[i][1]
        p_list = test_cases[i][2]

        total_presses = [0] * 26
        last_correct_press = 0
        for p in p_list + [n]:
            current_presses = [0] * 26
            for j in range(last_correct_press, p):
                current_presses[ord(s[j]) - ord('a')] += 1

            for j in range(26):
                total_presses[j] += current_presses[j]

            last_correct_press = p

        print(' '.join(map(str, total_presses)))

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    p_list = list(map(int, input().split()))
    test_cases.append((n, m, s, p_list))

# Call the function with the input
calculate_button_presses(t, test_cases)
