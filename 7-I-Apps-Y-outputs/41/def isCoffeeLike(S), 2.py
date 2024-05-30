
def isCoffeeLike(S):
    return S[2] == S[3] and S[4] == S[5]

S = input()
print("Yes" if isCoffeeLike(S) else "No")

