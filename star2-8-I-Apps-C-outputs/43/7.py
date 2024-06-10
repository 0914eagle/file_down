
n = int(input())
s = input()

def count_alternating_subsequence(s):
    alternating_subsequence_length = 0
    prev_char = ''
    for char in s:
        if char != prev_char:
            alternating_subsequence_length += 1
            prev_char = char
    return alternating_subsequence_length

max_alternating_subsequence_length = count_alternating_subsequence(s)
for i in range(n):
    new_char = '0' if s[i] == '1' else '1'
    new_string = s[:i] + new_char + s[i+1:]
    alternating_subsequence_length = count_alternating_subsequence(new_string)
    if alternating_subsequence_length > max_alternating_subsequence_length:
        max_alternating_subsequence_length = alternating_subsequence_length

print(max_alternating_subsequence_length)

