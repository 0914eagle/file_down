
m, d = map(int, input().split())
a = input()
b = input()

def find_magic_numbers(m, d, a, b):
  a = int(a)
  b = int(b)
  count = 0
  for i in range(a, b+1):
    if i % m != 0:
      continue
    
    i_str = str(i)
    odd_digits = [int(i_str[j]) for j in range(len(i_str)) if j % 2 == 0]
    if d in odd_digits:
      count += 1
  return count

print(find_magic_numbers(m, d, a, b) % (10**9 + 7))

