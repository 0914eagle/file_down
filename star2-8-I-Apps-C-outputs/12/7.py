
import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    
    if n == 1 or m == 1:
        print(max(n, m) // 3 * 2)
    else:
        print(n // 3 * m // 3 * 8)
    
if __name__ == "__main__":
    main()
    

