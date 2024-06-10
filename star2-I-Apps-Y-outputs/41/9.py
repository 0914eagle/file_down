
import sys

def is_halloween(month, day):
    if month == "OCT" and day == 31:
        return True
    if month == "DEC" and day == 25:
        return True
    return False

def main():
    month, day = sys.stdin.read().split()
    day = int(day)
    if is_halloween(month, day):
        print("yup")
    else:
        print("nope")

if __name__ == "__main__":
    main()

