
#python3
def compute_lps_array(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(pattern, text):
    lps = compute_lps_array(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return True
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

def longest_common_substring(s1, s2):
    max_len = 0
    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            if kmp_search(s1[i:j], s2):
                max_len = max(max_len, j - i)
    return max_len

def longest_substring(strings):
    max_len = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings) + 1):
            len_common = 0
            for k in range(i, j):
                len_common = max(len_common, longest_common_substring(strings[k], strings[k + 1]))
            max_len = max(max_len, len_common)
    return max_len

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

print(longest_substring(strings))
