
#1
N, P = map(float, input().split())
energy = [0 for i in range(int(N))]
prob = [0 for i in range(int(N))]
for i in range(int(N)):
    energy[i], prob[i] = map(float, input().split())
    if prob[i] >= P:
        print(int(energy[i]))
        break
else:
    print(-1)
