
n, l = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

def potato(a, c, l):
  total_price = sum(c)
  total_quantity = sum(a)
  first_store_quantity = 0
  second_store_quantity = 0
  for i in range(len(a)):
    if first_store_quantity + a[i] <= l:
      first_store_quantity += a[i]
    else:
      second_store_quantity += a[i]
  first_store_price = total_price / first_store_quantity
  second_store_price = total_price / second_store_quantity
  return first_store_price * second_store_price

print(f'{potato(a, c, l):.3f}')

