
s = input()

missing = [False]*26
for c in s:
    if c == "?":
        continue
    missing[ord(c) - ord("A")] = True

if all(missing):
    print(-1)
    exit()

for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if not missing[ord(c) - ord("A")]:
        s = s.replace("?", c, 1)
        missing[ord(c) - ord("A")] = True
        if all(missing):
            print(s)
            exit()

print(-1)

