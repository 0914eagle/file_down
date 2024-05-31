
def check_typing_pairs(n, pairs):
    output = []
    for i in range(n):
        s, t = pairs[i]
        if len(t) < len(s):
            output.append("NO")
        else:
            j = 0
            for letter in t:
                if j < len(s) and letter == s[j]:
                    j += 1
            if j == len(s):
                output.append("YES")
            else:
                output.append("NO")
    return output

# Read input
n = int(input())
pairs = []
for _ in range(n):
    s = input().strip()
    t = input().strip()
    pairs.append((s, t))

# Check typing pairs
output = check_typing_pairs(n, pairs)

# Output the result
for result in output:
    print(result)
