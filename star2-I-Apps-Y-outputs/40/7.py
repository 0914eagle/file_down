
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def calc_time(order_time, dish_time):
  if order_time % 10 == 0:
    return order_time + dish_time
  else:
    return order_time + 10 - (order_time % 10) + dish_time

order_time = 0
order_time = calc_time(order_time, A)
order_time = calc_time(order_time, B)
order_time = calc_time(order_time, C)
order_time = calc_time(order_time, D)
order_time = calc_time(order_time, E)

print(order_time)

