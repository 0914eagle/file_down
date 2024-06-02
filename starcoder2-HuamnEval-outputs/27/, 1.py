
class Solution:
    def evenOddPalindrome(self, n):
        
        even, odd = 0, 0
        for i in range(1, n+1):
            if self.isPalindrome(i):
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return (even, odd)

    def isPalindrome(self, n):
        n = str(n)
        return n == n[::-1]
 