
[SOL]
def ruler_marks(n, l, x, y, a):
  def get_closest_mark(d):
    left = 0
    right = n - 1
    while left <= right:
      mid = left + (right - left) // 2
      if a[mid] == d:
        return mid
      elif a[mid] < d:
        left = mid + 1
      else:
        right = mid - 1
    return left

  marks = []
  marks.append(get_closest_mark(x))
  marks.append(get_closest_mark(y))
  marks = sorted(marks)
  v = 0
  for i in range(1, len(marks)):
    v += marks[i] - marks[i - 1] - 1
  p = []
  for i in range(1, len(marks)):
    for j in range(marks[i - 1] + 1, marks[i]):
      p.append(a[j])

  return v, p
[/SOL]

