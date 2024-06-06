
import sys

def main():
    line = sys.stdin.readline().strip()
    if line.endswith("po"):
        print("FILIPINO")
    elif line.endswith("desu") or line.endswith("masu"):
        print("JAPANESE")
    else:
        print("KOREAN")

main()
