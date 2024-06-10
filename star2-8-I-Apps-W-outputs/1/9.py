
from sys import stdin

def main():
    w, h, k = map(int, stdin.readline().split())
    if w <= 0 or h <= 0 or k <= 0:
        return 0
    if w > 100 or h > 100:
        return 0
    if k > min(w, h) // 4:
        return 0
    
    rings = 0
    for i in range(k):
        rings += (w - 2 * i) * 2 + (h - 2 * i) * 2 - 4
    
    return rings

if __name__ == "__main__":
    print(main())

