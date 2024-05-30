
def min_operations(s):
    # your code goes here
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'a':
                count += 1
        else:
            if s[i] == 'b':
                count += 1
    return count


def modify(s):
    # your code goes here
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'a':
                s[i] = 'b'
        else:
            if s[i] == 'b':
                s[i] = 'a'
    return s


n = int(input())
s = input()

print(min_operations(s))
print(''.join(modify(list(s))))

