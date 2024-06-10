
def get_max_blue_lemonade(children, start, end):
  max_blue_lemonade = 0

  for i in range(start, end):
    child = children[i]
    offered_lemonade, wanted_lemonade, exchange_rate = child

    if offered_lemonade == "pink":
      max_blue_lemonade += exchange_rate

  return max_blue_lemonade


def exchange_lemonade(children, start, end):
  max_blue_lemonade = get_max_blue_lemonade(children, start, end)

  if max_blue_lemonade > 10:
    max_blue_lemonade = 10

  return max_blue_lemonade


if __name__ == "__main__":
  num_children = int(input())
  children = []

  for _ in range(num_children):
    offered_lemonade, wanted_lemonade, exchange_rate = input().split()
    exchange_rate = float(exchange_rate)
    children.append((offered_lemonade, wanted_lemonade, exchange_rate))

  max_blue_lemonade = exchange_lemonade(children, 0, len(children))
  print(max_blue_lemonade)

