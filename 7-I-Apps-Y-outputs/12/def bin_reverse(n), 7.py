
def bin_reverse(n):
    return int(str(n)[::-1], 2)

def main():
    n = int(input())
    print(bin_reverse(n))

if __name__ == "__main__":
    main()

