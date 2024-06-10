
def check_safety(yards):
    if yards <= -20:
        return True
    return False


def check_touchdown(yards):
    if yards >= 80:
        return True
    return False


def check_first_down(yards):
    if yards >= 10:
        return True
    return False


n = int(input())
yards = 0
touchdown = False
safety = False

for i in range(n):
    play_yards = int(input())
    yards += play_yards
    if check_touchdown(yards):
        touchdown = True
        break
    if check_first_down(yards):
        yards = 0
    if check_safety(yards):
        safety = True
        break

if touchdown:
    print("Touchdown")
elif safety:
    print("Safety")
else:
    print("Nothing")

