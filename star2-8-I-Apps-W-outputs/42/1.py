
def is_d_magic(num, d):
  num_str = str(num)
  return (
    all(
      (i % 2 == 0 and int(num_str[i]) == d)
      or (i % 2 != 0 and int(num_str[i]) != d)
      for i in range(len(num_str))
    )
    and num % d == 0
  )


def count_d_magic(a, b, d, m):
  return sum(1 for i in range(a, b + 1) if is_d_magic(i, d) and i % m == 0)


m, d = map(int, input().split())
a = int(input())
b = int(input())

print(count_d_magic(a, b, d, m) % (10 ** 9 + 7))

