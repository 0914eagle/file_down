
numPlays = int(input())
yards = [int(x) for x in input().split()]

yardsGained = 0
possession = 0

for i in range(numPlays):
    possession += yards[i]
    yardsGained += yards[i]
    if possession >= 100:
        print("Touchdown")
        break
    elif possession <= 0:
        print("Safety")
        break

if possession > 0 and possession < 100:
    print("Nothing")

