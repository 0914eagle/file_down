
def min_operations(s):
    count_a = 0
    count_b = 0
    count_operations = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count_a += 1
        else:
            count_b += 1
        if i % 2 == 1:
            if count_a != count_b:
                count_operations += 1
                if count_a > count_b:
                    count_a -= 1
                    count_b += 1
                else:
                    count_a += 1
                    count_b -= 1
    return count_operations


def modify_string(s):
    count_a = 0
    count_b = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count_a += 1
        else:
            count_b += 1
        if i % 2 == 1:
            if count_a != count_b:
                if count_a > count_b:
                    s[i] = 'b'
                else:
                    s[i] = 'a'
    return ''.join(s)


n = int(input())
s = input()
count_operations = min_operations(s)
print(count_operations)
print(modify_string(s))

