
import math

def get_magic_number_count(m, d, a, b):
  magic_number_count = 0
  a_length = len(a)
  b_length = len(b)
  a_digit_count = [0] * 10
  b_digit_count = [0] * 10
  for digit in a:
    a_digit_count[int(digit)] += 1
  for digit in b:
    b_digit_count[int(digit)] += 1
  for i in range(10):
    if i == d:
      magic_number_count += (b_digit_count[i] - a_digit_count[i]) // (2 * m)
    else:
      magic_number_count += (b_digit_count[i] - a_digit_count[i]) // m
  return magic_number_count

m, d = map(int, input().split())
a = input()
b = input()

magic_number_count = get_magic_number_count(m, d, a, b)

print(magic_number_count % (10**9 + 7))

