
def solve_combo(t, test_cases):
    for i in range(t):
        n, m = test_cases[i][0]
        s = test_cases[i][1]
        p = test_cases[i][2]

        presses = [0] * 26
        last_correct_idx = 0
        mistake_count = 0

        for idx, letter in enumerate(s):
            letter_idx = ord(letter) - ord('a')
            presses[letter_idx] += 1

            if idx < last_correct_idx:
                continue
        
            if mistake_count < m and idx + 1 == p[mistake_count]:
                last_correct_idx = 0
                mistake_count += 1
            else:
                last_correct_idx = idx
        
        print(" ".join(map(str, presses)))


t = 3
test_cases = [
    ((4, 2), "abca", [1, 3]),
    ((10, 5), "codeforces", [2, 8, 3, 2, 9]),
    ((26, 10), "qwertyuioplkjhgfdsazxcvbnm", [20, 10, 1, 2, 3, 5, 10, 5, 9, 4])
]

solve_combo(t, test_cases)
```
