
n = int(input())

def get_num_digits(num):
  num_digits = 0
  while num > 0:
    num //= 10
    num_digits += 1
  return num_digits

def get_lucky_num(digits):
  num = 0
  for i in range(digits):
    num = num * 10 + 8
  return num

def get_num_lucky_nums(digits):
  if digits == 1:
    return 2
  return 10 * get_num_lucky_nums(digits - 1)

max_num = get_lucky_num(n)
num_digits = get_num_digits(max_num)

print(get_num_lucky_nums(num_digits))

