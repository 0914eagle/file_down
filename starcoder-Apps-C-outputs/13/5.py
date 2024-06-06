
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import permutations

wordlist = ["be","our","rum","will","dead","hook","ship","blood","sable","avenge","parrot","captain"]
text = input()
text_list = text.split(" ")

for i in range(len(text_list)):
    for j in range(len(text_list[i])):
        text_list[i] = text_list[i].replace(text_list[i][j],"_")
        
letters = [item for sublist in text_list for item in sublist]

ans = 0
for perm in permutations(wordlist,len(text_list)):
    ans = 1
    for i in range(len(text_list)):
        for j in range(len(text_list[i])):
            if len(set(text_list[i])) != len(set(perm[i])):
                ans = 0
                break
            else:
                for k in range(len(text_list[i])):
                    if text_list[i][k] == "_":
                        text_list[i] = text_list[i].replace(text_list[i][k],perm[i][k])
    if ans == 1:
        break

if ans == 1:
    print(" ".join(text_list))
else:
    print("Impossible")
