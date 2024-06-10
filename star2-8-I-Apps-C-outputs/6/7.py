
import sys
input = sys.stdin.readline

def get_max_blue(N, offers):
    offers = sorted(offers, key=lambda x: x[2])
    ratio = 1.0
    max_blue = 0.0
    for i in range(N):
        if offers[i][1] == "pink":
            max_blue += ratio
        else:
            ratio *= offers[i][2]
    if max_blue > 10.0:
        max_blue = 10.0
    return max_blue

N = int(input())
offers = []
for _ in range(N):
    O, W, R = input().split()
    R = float(R)
    offers.append((O, W, R))

print(get_max_blue(N, offers))

