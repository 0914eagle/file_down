
from itertools import combinations
clauses = [(1,2,3), (1,-2,3), (-1,-2,3), (-1,-2,-3), (-1,2,-3)]
def check_clause(values, clause):
  if values[abs(clause[0])-1] == clause[0] / abs(clause[0]):
    return True
  if values[abs(clause[1])-1] == clause[1] / abs(clause[1]):
    return True
  if values[abs(clause[2])-1] == clause[2] / abs(clause[2]):
    return True
  return False
for values in combinations([1,1,1,-1,-1,-1], 3):
  satisfied = True
  for clause in clauses:
    if not check_clause(values, clause):
      satisfied = False
      break
  if satisfied:
    print("satisfactory")
    break
else:
  print("unsatisfactory")

