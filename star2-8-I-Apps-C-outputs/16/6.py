
import math
import sys
from collections import defaultdict

def find_poly(n):
    poly_a = []
    poly_b = []
    
    for i in range(n):
        poly_a.append(1)
    
    poly_a.append(0)
    poly_b.append(1)
    
    return (poly_a, poly_b)

def print_poly(poly):
    degree = len(poly) - 1
    
    print(degree)
    print(*poly)
    
if __name__ == "__main__":
    
    n = int(sys.stdin.readline().strip())
    
    poly_a, poly_b = find_poly(n)
    
    print_poly(poly_a)
    print_poly(poly_b)
    

