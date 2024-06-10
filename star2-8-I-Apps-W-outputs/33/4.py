
import sys
def parse_input(input_str):
  lines = input_str.split('\n')
  s1 = lines[0].strip()
  s2 = lines[1].strip()
  return s1, s2
def calculate_prob(s1, s2):
  pass
if __name__ == '__main__':
  s1, s2 = parse_input(sys.stdin.read())
  print(calculate_prob(s1, s2))

