
def time_before(hour, minute):
  new_hour = hour
  new_minute = minute
  new_minute -= 45
  if new_minute < 0:
    new_hour -= 1
    new_minute += 60
  if new_hour < 0:
    new_hour += 24
  print(new_hour, new_minute)


if __name__ == "__main__":
  hour, minute = [int(x) for x in input().split()]
  time_before(hour, minute)

