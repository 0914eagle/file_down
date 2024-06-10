
from sys import stdin


def readint():
    return int(stdin.readline())


def readints():
    return [int(x) for x in stdin.readline().split()]


def readstr():
    return stdin.readline().strip()


def readstrs():
    return stdin.readline().split()


n_usb, n_ps2, n_both = readints()

mice = []

for _ in range(readint()):
    mice.append(readints() + readstr().split())

mice = sorted(mice, key=lambda x: x[0])

i = 0
total_cost = 0
n_equipped = 0

while n_equipped < n_usb + n_both and i < len(mice):
    if mice[i][1] == "USB":
        total_cost += mice[i][0]
        n_equipped += 1
    i += 1

while n_equipped < n_usb + n_both + n_ps2 and i < len(mice):
    if mice[i][1] == "PS/2":
        total_cost += mice[i][0]
        n_equipped += 1
    i += 1

print(n_equipped, total_cost)

