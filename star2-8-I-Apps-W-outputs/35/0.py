
s = [input() for i in range(4)]
for i in range(4):
    for j in range(4):
        if s[i][j] == ".":
            s[i] = s[i][:j] + "#" + s[i][j + 1:]
        else:
            s[i] = s[i][:j] + "." + s[i][j + 1:]
        for p in range(2):
            for q in range(2):
                if s[i + p][j + q] != s[i][j]:
                    break
            else:
                continue
            break
        else:
            print("YES")
            exit()
        s[i] = s[i][:j] + "." + s[i][j + 1:]
print("NO")

