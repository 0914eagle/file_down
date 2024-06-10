
s = input()
q = int(input())

def distinct_characters_in_substring(s, l, r):
    distinct_chars = set()
    for i in range(l, r + 1):
        distinct_chars.add(s[i - 1])
    return len(distinct_chars)

for _ in range(q):
    query = input().split(' ')
    if query[0] == '1':
        s = s[:int(query[1]) - 1] + query[2] + s[int(query[1]):]
    else:
        print(distinct_characters_in_substring(s, int(query[1]), int(query[2])))


