
import sys

def is_halloween(date):
    month, day = date.split()
    if month == "OCT" and day == "31":
        return True
    if month == "DEC" and day == "25":
        return True
    return False

def main():
    date = sys.stdin.read().strip()
    if is_halloween(date):
        print("yup")
    else:
        print("nope")

if __name__ == "__main__":
    main()

