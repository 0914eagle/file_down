
# Python3 code for Modular 
# exponentiation 
 
# function to compute x^y under 
# modulo m 
def power(x, y, m): 
    if (y == 0): 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
      
    if(y % 2 == 0): 
        return p 
    else: 
        return ((x * p) % m) 
  
  
# Driver Code 
x = 2
y = 5
m = 13
print(power(x, y, m)) 
  
# This code is contributed by  

