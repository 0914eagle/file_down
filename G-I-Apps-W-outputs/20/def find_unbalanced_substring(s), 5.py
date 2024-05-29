
def find_unbalanced_substring(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            sub = s[i:j+1]
            count = {}
            for char in sub:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            max_count = max(count.values())
            if len(sub) >= 2 and max_count > len(sub)//2:
                return i+1, j+1
    return -1, -1

# Input
s = input().strip()

# Output
start, end = find_unbalanced_substring(s)
print(start, end)
