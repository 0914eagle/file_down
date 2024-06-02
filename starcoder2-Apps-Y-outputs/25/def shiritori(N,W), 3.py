
def shiritori(N,W):
    for i in range(N):
        if W[i] in W[i+1:]:
            return "No"
        if W[i][0] != W[i-1][-1]:
            return "No"
    return "Yes"

N = int(input())
W = []
for i in range(N):
    W.append(input())
print(shiritori(N,W))

