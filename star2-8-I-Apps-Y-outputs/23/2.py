
def count_distinct_chars(s, l, r):
    char_count = {}
    for char in s[l-1:r]:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return len(char_count)

s = input()
q = int(input())

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        s = s[:int(query[1])-1] + query[2] + s[int(query[1]):]
    else:
        print(count_distinct_chars(s, int(query[1]), int(query[2])))

