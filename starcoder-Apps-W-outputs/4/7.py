
t = int(input())
for i in range(t):
    x = input()
    if x[-2:] == "po":
        print("FILIPINO")
    elif x[-3:] == "desu" or x[-4:] == "masu":
        print("JAPANESE")
    else:
        print("KOREAN")
