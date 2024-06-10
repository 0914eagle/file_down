
def solve(a, b):
  def calculate_row_value(row, col):
    if col == 1:
      return row
    else:
      prev_col_value = calculate_row_value(row, col - 1)
      return prev_col_value + int(str(prev_col_value)[::-1])

  def calculate_table_value(row, col):
    if col < 1:
      return 0
    else:
      return calculate_row_value(row, col)

  def calculate_interval_value(a, b):
    lower_bound_row = a
    lower_bound_col = 0
    while calculate_table_value(lower_bound_row, lower_bound_col) < a:
      lower_bound_col += 1

    upper_bound_row = b
    upper_bound_col = 0
    while calculate_table_value(upper_bound_row, upper_bound_col) < b:
      upper_bound_col += 1

    if calculate_table_value(lower_bound_row, lower_bound_col) != a:
      lower_bound_row += 1
      lower_bound_col = 0

    if calculate_table_value(upper_bound_row, upper_bound_col) != b:
      upper_bound_row -= 1
      upper_bound_col = 0

    return (upper_bound_row - lower_bound_row + 1) * (upper_bound_col - lower_bound_col + 1)

  return calculate_interval_value(a, b)


if __name__ == "__main__":
  queries = int(input())
  for _ in range(queries):
    a, b = map(int, input().split())
    print(solve(a, b))

