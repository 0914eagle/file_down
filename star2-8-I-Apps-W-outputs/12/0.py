
import sys

def main():
    plays = int(sys.stdin.readline().strip())
    yards = [int(x) for x in sys.stdin.readline().strip().split()]
    
    total = 0
    for y in yards:
        total += y
    
    if total >= 80:
        print("Touchdown")
    elif total + 20 <= 0:
        print("Safety")
    else:
        print("Nothing")

if __name__ == '__main__':
    main()

