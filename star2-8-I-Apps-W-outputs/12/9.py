
import sys
lines = sys.stdin.readlines()
num_plays = int(lines[0])
yards_gained = [int(yards) for yards in lines[1].split()]
yards_gained = yards_gained[:num_plays]

total_yards = sum(yards_gained)
if total_yards >= 80:
    print('Touchdown')
elif total_yards <= -20:
    print('Safety')
else:
    print('Nothing')

