
import sys

input = sys.stdin.readline

def main():
    s = input().rstrip()
    num = int(s[1:])
    print(num // 1000)

if __name__ == "__main__":
    main()

