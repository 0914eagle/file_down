
def check_typing_pairs(n, pairs):
    result = []
    for i in range(n):
        s, t = pairs[i][0], pairs[i][1]
        s_index = 0
        t_index = 0
        s_length = len(s)
        t_length = len(t)

        while s_index < s_length and t_index < t_length:
            if s[s_index] != t[t_index]:
                result.append("NO")
                break
            s_count = 1
            t_count = 1
            while s_index + s_count < s_length and s[s_index] == s[s_index + s_count]:
                s_count += 1
            while t_index + t_count < t_length and t[t_index] == t[t_index + t_count]:
                t_count += 1
            if t_count < s_count:
                result.append("NO")
                break
            s_index += s_count
            t_index += t_count

        if s_index < s_length or t_index < t_length:
            result.append("NO")
        else:
            result.append("YES")

    return result


# Input processing
n = int(input())
pairs = []
for _ in range(n):
    s = input().strip()
    t = input().strip()
    pairs.append((s, t))

# Call the function
output = check_typing_pairs(n, pairs)

# Output the result
for res in output:
    print(res)
