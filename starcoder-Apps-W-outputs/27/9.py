
n = int(input())

names = []

for _ in range(n):
	names.append(input())

alpha = list("abcdefghijklmnopqrstuvwxyz")

for i in range(len(alpha)):
	alpha[i] = alpha[i] + " "

for i in range(len(names)-1):
	if len(names[i]) > len(names[i+1]):
		diff = len(names[i]) - len(names[i+1])
		for j in range(diff):
			names[i+1] = names[i+1] + " "
	else:
		diff = len(names[i+1]) - len(names[i])
		for j in range(diff):
			names[i] = names[i] + " "

#print(names)

flag = False

for i in range(len(names)-1):
	for j in range(len(names[i])):
		if alpha.index(names[i][j]) > alpha.index(names[i+1][j]):
			print("Impossible")
			flag = True
			break
		elif alpha.index(names[i][j]) < alpha.index(names[i+1][j]):
			break
	if flag == True:
		break

if flag == False:
	print("".join(alpha))
