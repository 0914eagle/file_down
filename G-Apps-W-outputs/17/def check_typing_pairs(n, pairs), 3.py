
def check_typing_pairs(n, pairs):
    def check_typing(s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return "NO"
            char_count_s = 1
            char_count_t = 1
            i_count = i + 1
            while i_count < len(s) and s[i_count] == s[i]:
                i_count += 1
                char_count_s += 1
            j_count = j + 1
            while j_count < len(t) and t[j_count] == t[j]:
                j_count += 1
                char_count_t += 1
            if char_count_t < char_count_s:
                return "NO"
            i = i_count
            j = j_count
        return "YES" if i == len(s) and j == len(t) else "NO"

    results = []
    for i in range(0, 2*n, 2):
        s = pairs[i]
        t = pairs[i + 1]
        results.append(check_typing(s, t))
    
    return results

# Input processing
n = int(input())
pairs = []
for _ in range(n):
    s = input().strip()
    t = input().strip()
    pairs.extend([s, t])

# Call the function and print the results
results = check_typing_pairs(n, pairs)
for res in results:
    print(res)
