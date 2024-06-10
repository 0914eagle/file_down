
def find_sequence(golorp):
  jaws = golorp.count("_")
  values = [str(i) for i in range(10)]
  min_value = "9" * jaws
  for value in values:
    if value * jaws <= min_value:
      min_value = value * jaws
  if min_value == "9" * jaws:
    return "false"
  return min_value

if __name__ == '__main__':
  golorp = input()
  print(find_sequence(golorp))


