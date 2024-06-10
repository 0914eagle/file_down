
def dreamoon(s1, s2):
  s1 = s1.replace("+", "1").replace("-", "0")
  s2 = s2.replace("+", "1").replace("-", "0").replace("?", "x")
  def check(s1, s2):
    for i in range(len(s1)):
      if s1[i] != s2[i] and s2[i] != "x":
        return False
    return True
  correct = 0
  for i in range(2**s2.count("x")):
    s2_copy = s2
    for j in range(s2.count("x")):
      if (i >> j) & 1:
        s2_copy = s2_copy[:j] + "1" + s2_copy[j+1:]
      else:
        s2_copy = s2_copy[:j] + "0" + s2_copy[j+1:]
    if check(s1, s2_copy):
      correct += 1
  return correct/2**s2.count("x")

