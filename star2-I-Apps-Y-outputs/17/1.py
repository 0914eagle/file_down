
S = input()
T = input()

for i in range(len(S)):
    if S == T:
        print("Yes")
        break
    else:
        S = S[-1] + S[:-1]
    if i == len(S) - 1:
        print("No")

