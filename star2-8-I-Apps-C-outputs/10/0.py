
def count_appearances(a, b):
  def get_digit_count(n):
    digit_count = 0
    while n > 0:
      digit_count += 1
      n //= 10
    return digit_count

  def get_num_with_digit_count(digit_count):
    num_with_digit_count = 0
    for i in range(1, digit_count + 1):
      num_with_digit_count = num_with_digit_count * 10 + i
    return num_with_digit_count

  total_count = 0
  current_num = 1
  while current_num <= b:
    digit_count = get_digit_count(current_num)
    num_with_digit_count = get_num_with_digit_count(digit_count)
    if a <= num_with_digit_count <= b:
      total_count += digit_count
    current_num += 1

  return total_count

q = int(input())
for _ in range(q):
  a, b = map(int, input().split())
  print(count_appearances(a, b))

