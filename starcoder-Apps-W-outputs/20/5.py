
# Differences
# Assume the birds are sorted by position
# Traverse through all positions of the birds and decide how many birds can be added
# The difference between the two positions should be at least 2*d + 6

# Implement
# Find all possible positions
# For each position, decide how many birds can be added
# The difference between two positions should be at least 2*d + 6
# Can be converted to a graph problem

from sys import stdin

def main():
  line = stdin.readline().strip().split()
  length = int(line[0])
  distance = int(line[1])
  num_birds = int(line[2])
  positions = sorted([int(stdin.readline().strip()) for _ in range(num_birds)])
  positions = [0] + positions + [length]

  max_add = 0
  for i in range(len(positions) - 1):
    if positions[i+1] - positions[i] > 2*distance + 6:
      max_add += (positions[i+1] - positions[i] - 6) // (distance + 6)
  print(max_add)

main()
