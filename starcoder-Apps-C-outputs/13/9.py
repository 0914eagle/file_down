
text = input()
#print(text)
common = [["be","our","rum","will","dead","hook","ship","blood","sable","avenge","parrot","captain"],["be","our","rum","will","dead","hook","ship","blood","sable","avenge","parrot","captain"]]

for i in range(len(text)):
    if text[i] == " ":
        pass
    else:
        for j in range(len(common[0])):
            for k in range(len(common[0][j])):
                if common[0][j][k] == text[i]:
                    common[1][j] = common[1][j][0:k] + common[0][j][k] + common[1][j][k+1:]
                    #print(common[1][j])
                    break
#print(common)

out = ""
for i in range(len(text)):
    if text[i] == " ":
        out += " "
    else:
        for j in range(len(common[0])):
            if common[0][j][0] == text[i]:
                out += common[0][j][0]
                #print(common[0][j][0])
                break
print(out)

