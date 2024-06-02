
def main():
    s, v1, v2 = map(int, input().split())
    if s % (v1 - v2) != 0:
        print("Impossible")
    else:
        print(s // (v1 - v2), s // v1)

if __name__ == "__main__":
    main()

