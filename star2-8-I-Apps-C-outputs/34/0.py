
class Solution:
  def solve(self, input):
    lines = input.split('\n')
    N = int(lines[0])
    numbers = list(map(int, lines[1:]))
    numbers.sort()
    
    for i in range(N-1, 1, -1):
      for j in range(i-1, 0, -1):
        num = numbers[i] - numbers[j]
        low = 0
        high = j-1
        
        while low <= high:
          mid = low + (high - low) // 2
          if numbers[mid] == num:
            return numbers[i]
          elif numbers[mid] < num:
            low = mid + 1
          else:
            high = mid - 1
    
    return 'no solution'

