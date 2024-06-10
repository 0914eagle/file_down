
import sys

def laundry_machine_count(socks, capacity, max_color_diff):
  socks.sort()

  num_machines = 1
  current_machine_count = 0
  current_machine_color = None

  for sock in socks:
    if current_machine_count == capacity:
      num_machines += 1
      current_machine_count = 0
      current_machine_color = None
    
    if current_machine_color is None or abs(sock - current_machine_color) <= max_color_diff:
      current_machine_count += 1
      current_machine_color = sock
    else:
      num_machines += 1
      current_machine_count = 1
      current_machine_color = sock

  return num_machines

def main():
  _, capacity, max_color_diff = map(int, sys.stdin.readline().split())
  socks = list(map(int, sys.stdin.readline().split()))

  print(laundry_machine_count(socks, capacity, max_color_diff))

if __name__ == '__main__':
  main()

