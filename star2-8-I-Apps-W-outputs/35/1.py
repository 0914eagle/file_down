
def solve(data):
  return 'YES' if any(is_rect(row, data) for row in range(len(data) - 1)) else 'NO'


def is_rect(row, data):
  for col in range(len(data[row]) - 1):
    if data[row][col] == data[row][col + 1] == data[row + 1][col] == data[row + 1][col + 1]:
      return True
  return False


if __name__ == '__main__':
  print(solve([input() for _ in range(4)]))

