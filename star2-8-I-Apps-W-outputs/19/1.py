
import string

alphabet = set(string.ascii_uppercase)

def is_nice(s):
    return set(s) == alphabet

def is_possible(s):
    return len(s) >= len(alphabet)

s = input()
if not is_possible(s):
    print(-1)
else:
    s = list(s)
    for i, c in enumerate(s):
        if c == '?':
            for ch in alphabet:
                s[i] = ch
                if is_nice(''.join(s)):
                    print(''.join(s))
                    break
            else:
                print(-1)
                break


